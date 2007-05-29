;--------------------------------
;Include Modern UI

  !include "MUI.nsh"

;--------------------------------
;General

  ;Name and file
  Name "Labyrinth"
  OutFile "labyrinth_installer_gtk.exe"

  ;Default installation folder
  InstallDir "$PROGRAMFILES\Labyrinth"

  ;Get installation folder from registry if available
  InstallDirRegKey HKCU "Software\Labyrinth" ""

;--------------------------------
;Interface Settings

  !define MUI_ABORTWARNING

;--------------------------------
;Pages

  !insertmacro MUI_PAGE_WELCOME
  !insertmacro MUI_PAGE_LICENSE "COPYING"
  !insertmacro MUI_PAGE_COMPONENTS
  !insertmacro MUI_PAGE_DIRECTORY
  !insertmacro MUI_PAGE_INSTFILES

  !insertmacro MUI_UNPAGE_WELCOME
  !insertmacro MUI_UNPAGE_CONFIRM
  !insertmacro MUI_UNPAGE_INSTFILES
  !insertmacro MUI_UNPAGE_FINISH
;--------------------------------
;Languages

  !insertmacro MUI_LANGUAGE "English"

;--------------------------------
;Installer Sections

Section "Labyrinth" SecApp

  SetOutPath $INSTDIR\data
  File "data\*.*"
  SetOutPath $INSTDIR\src
  File "src\*.*"
  SetOutPath $INSTDIR\po
  File "po\*.*"
  SetOutPath $INSTDIR
  File "dist\*.*"
  File "COPYING"

  ;Store installation folder
  WriteRegStr HKCU "Software\Labyrinth" "" $INSTDIR

  ;Create uninstaller
  WriteUninstaller "$INSTDIR\Uninstall.exe"

  CreateShortCut "$INSTDIR\Labyrinth.lnk" "$INSTDIR\labyrinth.exe"

  SetOutPath "$SMPROGRAMS\Labyrinth\"
  CopyFiles "$INSTDIR\Labyrinth.lnk" "$SMPROGRAMS\Labyrinth\"
  CopyFiles "$INSTDIR\Labyrinth.lnk" "$DESKTOP\"
  Delete "$INSTDIR\Labyrinth.lnk"
  CreateShortCut "$SMPROGRAMS\Labyrinth\Uninstall.lnk" "$INSTDIR\Uninstall.exe"

SectionEnd

Section "GTK+" SecGTK

  SetOutPath "$INSTDIR\"
  File "c:\GTK\bin\*.dll"

  SetOutPath "$INSTDIR\etc\fonts\"
  File "c:\GTK\etc\fonts\*.*"

  SetOutPath "$INSTDIR\etc\gtk-2.0\"
  File "c:\GTK\etc\gtk-2.0\*.*"

  SetOutPath "$INSTDIR\etc\pango\"
  File "c:\GTK\etc\pango\*.*"

  SetOutPath "$INSTDIR\lib\gtk-2.0\2.10.0\loaders\"
  File "c:\GTK\lib\gtk-2.0\2.10.0\loaders\*.*"

  SetOutPath "$INSTDIR\lib\gtk-2.0\2.10.0\engines\"
  File "c:\GTK\lib\gtk-2.0\2.10.0\engines\*.*"

  SetOutPath "$INSTDIR\lib\gtk-2.0\2.10.0\immodules\"
  File "c:\GTK\lib\gtk-2.0\2.10.0\immodules\*.*"

  SetOutPath "$INSTDIR\lib\pango\1.6.0\modules\"
  File "c:\GTK\lib\pango\1.6.0\modules\*.*"

  SetOutPath "$INSTDIR\share\themes\Default\gtk-2.0-key\"
  File "c:\GTK\share\themes\Default\gtk-2.0-key\*.*"

  SetOutPath "$INSTDIR\share\themes\MS-Windows\gtk-2.0\"
  File "c:\GTK\share\themes\MS-Windows\gtk-2.0\*.*"

SectionEnd

;--------------------------------
;Descriptions

  ;Language strings
  LangString DESC_SecApp ${LANG_ENGLISH} "Mind mapping for Gnome Desktop"
  LangString DESC_SecGTK ${LANG_ENGLISH} "Select if you don't have GTK+"

  ;Assign language strings to sections
  !insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
    !insertmacro MUI_DESCRIPTION_TEXT ${SecApp} $(DESC_SecApp)
    !insertmacro MUI_DESCRIPTION_TEXT ${SecGTK} $(DESC_SecGTK)
  !insertmacro MUI_FUNCTION_DESCRIPTION_END

;--------------------------------
;Uninstaller Section

Section "Uninstall"

  Delete "$INSTDIR\*.*"

  Delete "$DESKTOP\Labyrinth.lnk"
  Delete "$SMPROGRAMS\Labyrinth\Labyrinth.lnk"
  Delete "$SMPROGRAMS\Labyrinth\Uninstall.lnk"

  RMDir  "$SMPROGRAMS\Labyrinth\"

  RMDir /r "$INSTDIR\data\"
  RMDir /r "$INSTDIR\src\"
  RMDir /r "$INSTDIR\po\"   

  RMDir "$INSTDIR"

  DeleteRegKey /ifempty HKCU "Software\Labyrinth"

SectionEnd
