mv  ./tags ../tags
mv ../yuyujunjun-pages/tag ./tag
mv ../yuyujunjun-pages/author ./author
mv ../yuyujunjun-pages/sitemap.xml ./sitemap.xml
git add ./
git commit -m "upload blog"
git push origin master