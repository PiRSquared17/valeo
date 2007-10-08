;--------------------------------
;Include Modern UI

  !include "MUI.nsh"

;--------------------------------
;General

  ;Name and file
  Name "Labyrinth"
  OutFile "labyrinth_installer.exe"

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

;--------------------------------
;Descriptions

  ;Language strings
  LangString DESC_SecApp ${LANG_ENGLISH} "Mind mapping for Gnome Desktop"

  ;Assign language strings to sections
  !insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
    !insertmacro MUI_DESCRIPTION_TEXT ${SecApp} $(DESC_SecApp)
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
