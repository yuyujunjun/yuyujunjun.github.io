move  ./tags ../tags
move ../yuyujunjun-pages/tag ./tag
move ../yuyujunjun-pages/author ./author
move ../yuyujunjun-pages/tag/* ./tag/*
move ../yuyujunjun-pages/author/* ./author/*
move ../yuyujunjun-pages/sitemap.xml ./sitemap.xml
git add ./
git commit -m "upload blog"
git push origin master