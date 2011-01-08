mkdir C:\VCS\backup
rmdir /S /Q C:\VCS\backup
"C:\Arquivos de programas\VisualSVN Server\bin\svnadmin.exe" hotcopy C:\VCS\agenda C:\VCS\backup --clean-logs
xcopy C:\VCS\agenda C:\VCS\backup /E /I /Q /H /R /Y
pause