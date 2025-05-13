#!/usr/bin/env python
# coding: utf-8

# # Publications markdown generator for academicpages
# 
# Takes a set of bibtex of publications and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook ([see more info here](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)). 
# 
# The core python code is also in `pubsFromBibs.py`. 
# Run either from the `markdown_generator` folder after replacing updating the publist dictionary with:
# * bib file names
# * specific venue keys based on your bib file preferences
# * any specific pre-text for specific files
# * Collection Name (future feature)
# 
# TODO: Make this work with other databases of citations, 
# TODO: Merge this with the existing TSV parsing solution


from pybtex.database.input import bibtex
from pybtex.database import Person
import pybtex.database.input.bibtex 
from time import strptime
import string
import html
import os
import re

authors_info = {
    "Yiqian Wu": "https://onethousandwu.com",
    "Hao Xu": "https://xh38.github.io",
    "Xien Chen": "https://github.com/xienchenn",
    "Siyu Tang": "https://inf.ethz.ch/people/person-detail.MjYyNzgw.TGlzdC8zMDQsLTg3NDc3NjI0MQ==.html",
    "Xiaogang Jin" :"http://www.cad.zju.edu.cn/home/jin",
    "Yong-Liang Yang" : "https://www.yongliangyang.net/",
    "Xiaogang Jin" :"http://www.cad.zju.edu.cn/home/jin/",
    "Linjun Wu":"https://fivezerojun.github.io",
    "He Wang":"https://drhewang.com/"
}
my_name = "Xiangjun Tang"
#todo: incorporate different collection types rather than a catch all publications, requires other changes to template
publist = {
    "inproceedings": {
        "file" : "proceedings.bib",
        "venuekey": "booktitle",
        "venue-pretext": "In the proceedings of ",
        "collection" : {"name":"publications",
                        "permalink":"/publication/"}
        
    },
    "article":{
        "file": "pubs.bib",
        "venuekey" : "journal",
        "venue-pretext" : "",
        "collection" : {"name":"publications",
                        "permalink":"/publication/"}
    } 
}

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

    
def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)

def collect_from_folder(file_path):
    bibfile = os.path.join(file_path, "citation.txt")
    with open(bibfile, 'r', encoding='utf-8') as f:
        bib_content = f.read()
    markdown_item = {"collection":"publications","citation":f"/{bibfile}"}
    sub_items = os.listdir(file_path)
    content = None
    for item in sub_items:
        if "teaser" in item:
            markdown_item['teaser'] = os.path.join("/",file_path,item)
        if "main.pdf" == item:
            markdown_item["paperurl"] = os.path.join("/",file_path,item)
        if "appendix.pdf" == item:
            markdown_item["supplementary_materials"] = os.path.join("/",file_path,item)
        if "extra.json" == item:
            # extra_info = ['video','code','webpage']
            with open(os.path.join(file_path,item), 'r', encoding='utf-8') as f:
                extra = json.load(f)   
                for key in extra.keys():
                    # if key in extra_info:
                        markdown_item[key] = extra[key]
        if "content.md" == item:
            with open(os.path.join(file_path,item), 'r', encoding='utf-8') as f:
                content = f.read()
        
            
    assert content is not None or "project_page" in markdown_item.keys(), f"Missing content.md or project_page in {file_path}"
                # abstract = html_escape(abstract.replace("{", "").replace("}","").replace("\\",""))
    parser = bibtex.Parser()
    bibdata = parser.parse_file(bibfile)
    #loop through the individual references in a given bibtex file
    for bib_id in bibdata.entries:
        #reset default date
        pub_year = "1900"
        pub_month = "01"
        pub_day = "01"
        
        b = bibdata.entries[bib_id].fields
        original_type = bibdata.entries[bib_id].original_type # "inprocedding or article"
        try:
            markdown_item['title'] = html_escape(b["title"].replace("{", "").replace("}","").replace("\\",""))
            pub_year = f'{b["year"]}'
            #todo: this hack for month and day needs some cleanup
            if "month" in b.keys(): 
                if(len(b["month"])<3):
                    pub_month = "0"+b["month"]
                    pub_month = pub_month[-2:]
                elif(b["month"] not in range(12)):
                    tmnth = strptime(b["month"][:3],'%b').tm_mon   
                    pub_month = "{:02d}".format(tmnth) 
                else:
                    pub_month = str(b["month"])
            if "day" in b.keys(): 
                pub_day = str(b["day"])

                
            pub_date = pub_year+"-"+pub_month+"-"+pub_day
            markdown_item['date'] = pub_date
            markdown_item['year'] = pub_year
            #strip out {} as needed (some bibtex entries that maintain formatting)
            clean_title = b["title"].replace("{", "").replace("}","").replace("\\","").replace(" ","-")    
            url_slug = re.sub("\\[.*\\]|[^a-zA-Z0-9_-]", "", clean_title)
            url_slug = url_slug.replace("--","-")
            
            md_filename = (str(pub_year) + "-" + url_slug + ".md").replace("--","-")
            html_filename = (str(pub_year) + "-" + url_slug).replace("--","-")
            markdown_item["permalink"] = "/publication/" + html_filename
            #Build Citation from text
            citation = ""
            authors = ""
            #citation authors - todo - add highlighting for primary author?
            for i,author in enumerate(bibdata.entries[bib_id].persons["author"]):
                author = author.first_names[0] + " " + author.last_names[0]
                if i==0:
                    markdown_item['first_author'] = 'yes' if author == my_name else "no"
                if i!=0:
                    authors = authors + ", "
                if author == my_name:
                    author == f"**{author}**"
                if author in authors_info.keys():
                    authors = authors + f"[{author}]({authors_info[author]})"
                else:
                    authors = authors + author
            authors = authors + "."
            markdown_item['author'] = authors

            #citation title
            # citation = citation + "\"" + html_escape(b["title"].replace("{", "").replace("}","").replace("\\","")) + ".\""

            #add venue logic depending on citation type
            venue = b[publist[original_type]["venuekey"]].replace("{", "").replace("}","").replace("\\","")
            markdown_item['venue'] = venue
            
            citation = citation + " " + html_escape(venue)
            citation = citation + ", " + pub_year + "."

            md = "---"
            for key in markdown_item.keys():
                md += f"""\n{key}: \"{markdown_item[key]}\""""
            md += "\n---\n"
            if content is not None:
                md += f"{content}"
            md += f"\n\n**bibtex:**\n```\n{bib_content}\n```\n"
            # md += f"![teaser](\"{markdown_item['teaser']}\")"
            ## Markdown description for individual page
            md_filename = os.path.basename(md_filename)
            with open("./_publications/" + md_filename, 'w') as f:
                f.write(md)
            print(f'SUCESSFULLY PARSED {bib_id}: \"', b["title"][:60],"..."*(len(b['title'])>60),"\"")
        # field may not exist for a reference
        except KeyError as e:
            print(f'WARNING Missing Expected Field {e} from entry {bib_id}: \"', b["title"][:30],"..."*(len(b['title'])>30),"\"")
            continue
root_dir = "files/publications"
publist_path = os.listdir(root_dir)
import json

for path in publist_path:
    if ".DS_Store" in path:
        continue
    collect_from_folder(os.path.join(root_dir,path))