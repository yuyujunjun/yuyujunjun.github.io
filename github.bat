mv  ./tags ../tags
cp ../yuyujunjun-pages/tag ./tag
cp ../yuyujunjun-pages/author ./author
cp ../yuyujunjun-pages/sitemap.xml ./sitemap.xml
git add ./
git commit -m "upload blog"
git push origin master