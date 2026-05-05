1. renaming title for subsection.
2. replace section summary with transitions paragraph. 
3. just have summary for chapter not section.
4. provide full outline and template for each section so partner just fill in content. 
5. list all figures and tables we have. 
6. list all notation, symbol we used for consistent. 

for compile pdf:
```bash
cd C:\Users\ADMIN\Documents\GitHub\ARDG\report
powershell -ExecutionPolicy Bypass -File .\build.ps1
```

in macos:
```bash
cd ~/Documents/GitHub/ARDG/report
chmod +x build.sh
./build.sh
```

Clean generated files first
```bassh
cd ~/Documents/GitHub/ARDG/report
latexmk -C
```

Zip report folder
```bash
cd ~/Documents/GitHub/ARDG
zip -r report.zip report \
  -x "report/*.aux" \
     "report/*.log" \
     "report/*.out" \
     "report/*.toc" \
     "report/*.lof" \
     "report/*.lot" \
     "report/*.fls" \
     "report/*.fdb_latexmk" \
     "report/*.synctex.gz" \
     "report/main.pdf"
```