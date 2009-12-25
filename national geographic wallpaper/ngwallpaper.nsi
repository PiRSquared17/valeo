!include MUI.nsh
!include LogicLib.nsh
!include WinMessages.nsh
!include FileFunc.nsh
!include nsDialogs.nsh

RequestExecutionLevel admin
XPStyle on
SetOverwrite on 
ShowInstDetails show 

Name "National Geographic Wallpaper"
OutFile "ngwallpaper.exe"
InstallDir "$PROGRAMFILES\NationalGeographicWallpaper"

BrandingText "National Geographic Photo of the Day"

!define MUI_HEADERIMAGE
!define MUI_HEADERIMAGE_BITMAP "..\national geographic wallpaper\ng2.bmp"
!define MUI_ICON "..\national geographic wallpaper\ng.ico"
!define MUI_WELCOMEFINISHPAGE_BITMAP "..\national geographic wallpaper\ng3.bmp"
!define MUI_FINISHPAGE_NOAUTOCLOSE

!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_COMPONENTS
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_LANGUAGE "English"

Section "Python2.6" SecPython
  File "..\national geographic wallpaper\python-2.6.4.msi"
  ExecWait 'msiexec /i "python-2.6.4.msi" /passive '
SectionEnd

Section "Python PIL" SecPIL
  File "..\national geographic wallpaper\PIL-1.1.6.win32-py2.6.exe"
  ExecWait 'PIL-1.1.6.win32-py2.6.exe'
SectionEnd

Section "Python Win32" SecPyWin
  File "..\national geographic wallpaper\pywin32-214.win32-py2.6.exe"	
  ExecWait 'pywin32-214.win32-py2.6.exe'
SectionEnd

Section "NG WallPaper" SecNG
  CreateDirectory "$PROGRAMFILES\NationalGeographicWallpaper"
  SetOutPath "$INSTDIR"
  File "..\national geographic wallpaper\ngdesktopwallpaper.pyw"
  CreateShortCut "$SMSTARTUP\National Geographic Wallpaper.lnk" "$INSTDIR\ngdesktopwallpaper.pyw"
SectionEnd

#--------------------------------
# Descrição dos programas
!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
!insertmacro MUI_DESCRIPTION_TEXT ${SecPython} "Python 2.6 install" 
!insertmacro MUI_DESCRIPTION_TEXT ${SecPIL} "Python Imaging Library install" 
!insertmacro MUI_DESCRIPTION_TEXT ${SecPyWin} "Python Windows Extencions install" 
!insertmacro MUI_DESCRIPTION_TEXT ${SecNG} "National Geographic Wallpaper install" 
!insertmacro MUI_FUNCTION_DESCRIPTION_END
