!include MUI.nsh
!include LogicLib.nsh
!include WinMessages.nsh
!include FileFunc.nsh
!include nsDialogs.nsh

Function Inicio
	System::Call "User32::SetWindowPos(i, i, i, i, i, i, i) i ($HWNDPARENT, 0, 0, 0, 0, 0, 0x201)"
FunctionEnd
Section "-PosicaoTela"
	Call Inicio
SectionEnd

Function "Test"
	CreateDirectory "$INSTDIR"
FunctionEnd

#--------------------------------
# Privil�gios de usu�rio para instala��o no Windows Vista
RequestExecutionLevel admin

XPStyle on
Name "Test"
OutFile "Test.exe"
InstallDir "C:\Test"

#--------------------------------
# Texto do rodap�
BrandingText "Test"

#--------------------------------
# Logotipo no topo
!define MUI_HEADERIMAGE
!define MUI_HEADERIMAGE_BITMAP "..\Test\Imagens\Test.bmp"
!define MUI_ICON "..\Test\Imagens\icone.ico"
!define MUI_WELCOMEFINISHPAGE_BITMAP "..\Test\Imagens\Test.bmp"
!define MUI_FINISHPAGE_NOAUTOCLOSE

#--------------------------------
# P�ginas
Page custom nsDialogsWelcome
#!insertmacro MUI_PAGE_DIRECTORY # Escolha do diret�rio de instala��o do Test, padr�o C:\Test
!insertmacro MUI_PAGE_COMPONENTS
!insertmacro MUI_PAGE_INSTFILES

#--------------------------------
# Defini��o l�ngua
!insertmacro MUI_LANGUAGE "PortugueseBR"

# Verifica se j� foi aberto janela de instala��o
Var DIALOG
Var HEADLINE
Var TEXT
Var IMAGECTL
Var IMAGE
Var HEADLINE_FONT

Function .onInit

    CreateFont $HEADLINE_FONT "$(^Font)" "14" "500"
    System::Call 'kernel32::CreateMutexA(i 0, i 0, t "myMutex") i .r1 ?e'
    Pop $R0
    StrCmp $R0 0 +3
    MessageBox MB_OK|MB_ICONEXCLAMATION "O Test j� est� sendo instalado neste computador!"
    Abort
    CreateFont $HEADLINE_FONT "$(^Font)" "14" "500"
    InitPluginsDir
    File /oname=$TEMP\Test.bmp "..\Test\Imagens\Test.bmp"
  
FunctionEnd

#--------------------------------
# Esconder controles da tela de in�cio
Function HideControls

    LockWindow on
    GetDlgItem $0 $HWNDPARENT 1028
    ShowWindow $0 ${SW_HIDE}

    GetDlgItem $0 $HWNDPARENT 1256
    ShowWindow $0 ${SW_HIDE}

    GetDlgItem $0 $HWNDPARENT 1035
    ShowWindow $0 ${SW_HIDE}

    GetDlgItem $0 $HWNDPARENT 1037
    ShowWindow $0 ${SW_HIDE}

    GetDlgItem $0 $HWNDPARENT 1038
    ShowWindow $0 ${SW_HIDE}

    GetDlgItem $0 $HWNDPARENT 1039
    ShowWindow $0 ${SW_HIDE}

    GetDlgItem $0 $HWNDPARENT 1045
    ShowWindow $0 ${SW_NORMAL}
    LockWindow off
FunctionEnd

Function ShowControls

    LockWindow on
    GetDlgItem $0 $HWNDPARENT 1028
    ShowWindow $0 ${SW_NORMAL}

    GetDlgItem $0 $HWNDPARENT 1256
    ShowWindow $0 ${SW_NORMAL}

    GetDlgItem $0 $HWNDPARENT 1035
    ShowWindow $0 ${SW_NORMAL}

    GetDlgItem $0 $HWNDPARENT 1037
    ShowWindow $0 ${SW_NORMAL}

    GetDlgItem $0 $HWNDPARENT 1038
    ShowWindow $0 ${SW_NORMAL}

    GetDlgItem $0 $HWNDPARENT 1039
    ShowWindow $0 ${SW_NORMAL}

    GetDlgItem $0 $HWNDPARENT 1045
    ShowWindow $0 ${SW_HIDE}
    LockWindow off
FunctionEnd

#--------------------------------
# Texto da tela de in�cio
Function nsDialogsWelcome

    nsDialogs::Create 1044
    Pop $DIALOG

    nsDialogs::CreateControl STATIC ${WS_VISIBLE}|${WS_CHILD}|${WS_CLIPSIBLINGS}|${SS_BITMAP} 0 0 0 109u 193u ""
    Pop $IMAGECTL

    StrCpy $0 "..\Test\Imagens\Test.bmp"
    System::Call 'user32::LoadImage(i 0, t r0, i ${IMAGE_BITMAP}, i 0, i 0, i ${LR_LOADFROMFILE}) i.s'
    Pop $IMAGE
	
    SendMessage $IMAGECTL ${STM_SETIMAGE} ${IMAGE_BITMAP} $IMAGE

    nsDialogs::CreateControl STATIC ${WS_VISIBLE}|${WS_CHILD}|${WS_CLIPSIBLINGS} 0 115u 5u -130u 20u "IMPORTANTE !!!"
    Pop $HEADLINE

    CreateFont $1 "Verdana" "18" "650" /UNDERLINE
    SendMessage $HEADLINE ${WM_SETFONT} $1 1

    nsDialogs::CreateControl STATIC ${WS_VISIBLE}|${WS_CHILD}|${WS_CLIPSIBLINGS} 0 115u 25u -130u -20u "$\r$\n(...).$\r$\n$\r$\n(...)$\r$\n$\r$\n (...) $\n www.test.com.br $\n E-mail: test@Test.com.br $\n "
    Pop $TEXT
	
    SetCtlColors $DIALOG "" 0xffffff
    SetCtlColors $HEADLINE "" 0xffffff
    SetCtlColors $TEXT "" 0xffffff

    Call HideControls
    nsDialogs::Show
    Call ShowControls
    System::Call gdi32::DeleteObject(i$IMAGE)
FunctionEnd

#-----------------------------
# Programas a instalar

# Sobrep�e arquivos j� existentes
SetOverwrite on 
# N�o mostrar mensagens do progresso da instala��o para n�o ficar vis�vel a senha de dba
ShowInstDetails nevershow 

#----------------------------
# Sybase
Section "Sybase" SecSybase
	
    DetailPrint "Instalando o Sybase, aguarde....."
    MessageBox MB_OK 'Na pr�xima tela, escolha o pa�s "Brazil", marque a op��o "I accept" em seguida clique sobre o bot�o "Next".$\r$\n'

    ExecWait '..\Test\Sybase\setup.exe'
	
    DetailPrint "Instala��o do Sybase .....conclu�do!"

    DetailPrint "Instalando a 1� atualiza��o do Sybase, aguarde....."
    ExecWait '..\Test\Atualiza��o1\setup.exe'
    DetailPrint "Instala��o da 1� atualiza��o do Sybase .....conclu�do!"
    DetailPrint ""

    DetailPrint "Instalando a 2� atualiza��o do Sybase, aguarde....."
    ExecWait '..\Test\Atualiza��o2\setup.exe'
    DetailPrint "Instala��o da 2� atualiza��o do Sybase .....conclu�do!"
    DetailPrint ""
SectionEnd

#----------------------------
# ODBC
Section "Configura��o do ODBC" SecOdbc
    WriteRegStr HKLM "Software\ODBC\ODBC.INI\ODBC Data Sources" "Test" "Adaptive Server Anywhere 9.0"
    WriteRegStr HKLM "Software\ODBC\ODBC.INI\Test" "Driver" "$PROGRAMFILES\Sybase\SQL Anywhere 9\win32\dbodbc9.dll"
    WriteRegStr HKLM "Software\ODBC\ODBC.INI\Test" "EngineName" "BDTest"
    WriteRegStr HKLM "Software\ODBC\ODBC.INI\Test" "AutoStop" "Yes"
    WriteRegStr HKLM "Software\ODBC\ODBC.INI\Test" "Integrated" "No"
    WriteRegStr HKLM "Software\ODBC\ODBC.INI\Test" "Debug" "No"
    WriteRegStr HKLM "Software\ODBC\ODBC.INI\Test" "DisableMultiRowFetch" "No"
    WriteRegStr HKLM "Software\ODBC\ODBC.INI\Test" "CommLinks" "SharedMemory,TCPIP{}"
    WriteRegStr HKLM "Software\ODBC\ODBC.INI\Test" "Compress" "No"
    WriteRegStr HKLM "Software\ODBC\ODBC.INI\Test" "Delphi" "Yes"
    WriteRegStr HKLM "Software\Borland\Database Engine\Settings\DRIVERS\SYBASE\DB OPEN" "TDS PACKET SIZE" "8192"
    DetailPrint "Configura��o do ODBC .....conclu�do!"
    DetailPrint ""
SectionEnd

#----------------------------
# BDE
Section "BDE" SecBde
    DetailPrint "Instalando o BDE, aguarde....."
    ExecWait '..\Test\BDE\SETUP.EXE'
    Sleep 15000 # 15 segundos para instalar BDE
    CreateDirectory "$PROGRAMFILES\Borland\Common Files\BDE\"
    File "/oname=$PROGRAMFILES\Borland\Common Files\BDE\IDAPI.CFG" ..\Test\BDE\IDAPI.CFG
    File "/oname=$PROGRAMFILES\Borland\Common Files\BDE\IDAPI32.CFG" ..\Test\BDE\IDAPI32.CFG
    DetailPrint "Instala��o do BDE .....conclu�do!"
    DetailPrint ""
SectionEnd

#----------------------------
# Configura��o do formato de Data
Section "Configura��o de Data" SecData
    WriteRegStr HKCU "Control Panel\International" "sShortDate" "dd/MM/yyyy"
    WriteRegStr HKU ".DEFAULT\Control Panel\International" "sShortDate" "dd/MM/yyyy"
    WriteRegStr HKU "S-1-5-18\Control Panel\International" "sShortDate" "dd/MM/yyyy"
    WriteRegStr HKU "S-1-5-19\Control Panel\International" "sShortDate" "dd/MM/yyyy"
    WriteRegStr HKU "S-1-5-20\Control Panel\International" "sShortDate" "dd/MM/yyyy"
    DetailPrint "Configura��o do formato de data .....conclu�do!"
    DetailPrint ""
SectionEnd

#----------------------------
# DllInsc32 na pasta system32

Section "DllInscE32.dll" SecInsc
    File /oname=$SYSDIR\DllInscE32.dll "..\Test\dll\DllInscE32.dll"
    DetailPrint "Instala��o da DllInsc32 ..... conclu�do!"
    DetailPrint ""
SectionEnd

#----------------------------
# Criando atalho do Test para esta��es
Section "Atalhos para Esta��o" SecEstacao

    # Cria pasta C:\Test
    Call Test

    Exec '"$PROGRAMFILES\Sybase\SQL Anywhere 9\win32\dblang.exe" -q PT'
    File /oname=$INSTDIR\TestBAR_SENHA.exe "..\Test\Execut�veis\Test.exe"

    File /oname=$INSTDIR\BemaFI32.dll "..\Test\dll\BemaFI32.dll"
    File /oname=$INSTDIR\BioNetAcsDLL.dll "..\Test\dll\BioNetAcsDLL.dll"
    File /oname=$INSTDIR\borlndmm.dll "..\Test\dll\borlndmm.dll"
    File /oname=$INSTDIR\CapPluginCertis.dll "..\Test\dll\CapPluginCertis.dll"
    File /oname=$INSTDIR\CapPluginCrossMatch.dll "..\Test\dll\CapPluginCrossMatch.dll"
    File /oname=$INSTDIR\CapPluginFingercap.dll "..\Test\dll\CapPluginFingercap.dll"
    File /oname=$INSTDIR\CapPluginHamster.dll "..\Test\dll\CapPluginHamster.dll"
    File /oname=$INSTDIR\CertisExports.dll "..\Test\dll\CertisExports.dll"
    File /oname=$INSTDIR\CONVECF95.dll "..\Test\dll\CONVECF95.dll"
    File /oname=$INSTDIR\CONVECF.dll "..\Test\dll\CONVECF.dll"
    File /oname=$INSTDIR\CONVERSOR.dll "..\Test\dll\CONVERSOR.dll"
    File /oname=$INSTDIR\DAO350.DLL "..\Test\dll\DAO350.DLL"
    File /oname=$INSTDIR\Daruma32.dll "..\Test\dll\Daruma32.dll"
    File /oname=$INSTDIR\DLLG2.dll "..\Test\dll\DLLG2.dll"
    File /oname=$INSTDIR\dbxmys30.dll "..\Test\dll\dbxmys30.dll"
    File /oname=$INSTDIR\DllInscE32.dll "..\Test\dll\DllInscE32.dll"
    File /oname=$INSTDIR\dpDevClt.dll "..\Test\dll\dpDevClt.dll"
    File /oname=$INSTDIR\dpDevDat.dll "..\Test\dll\dpDevDat.dll"
    File /oname=$INSTDIR\dpFpFns.dll "..\Test\dll\dpFpFns.dll"
    File /oname=$INSTDIR\dpFtrEx.dll "..\Test\dll\dpFtrEx.dll"
    File /oname=$INSTDIR\dpMatch.dll "..\Test\dll\dpMatch.dll"
    File /oname=$INSTDIR\Grafico.dll "..\Test\dll\Grafico.dll"
    File /oname=$INSTDIR\GrFinger.dll "..\Test\dll\GrFinger.dll"
    File /oname=$INSTDIR\GrFingerJava.dll "..\Test\dll\GrFingerJava.dll"
    File /oname=$INSTDIR\GrFingerX.dll "..\Test\dll\GrFingerX.dll"
    File /oname=$INSTDIR\Id3BiokeyDll.dll "..\Test\dll\Id3BiokeyDll.dll"
    File /oname=$INSTDIR\Imprime.dll "..\Test\dll\Imprime.dll"
    File /oname=$INSTDIR\TestRES.dll "..\Test\dll\TestRES.dll"
    File /oname=$INSTDIR\libmySQL.dll "..\Test\dll\libmySQL.dll"
    File /oname=$INSTDIR\Midas.dll "..\Test\dll\Midas.dll"
    File /oname=$INSTDIR\MP20FI32.DLL "..\Test\dll\MP20FI32.DLL"
    File /oname=$INSTDIR\NBioBSP.dll "..\Test\dll\NBioBSP.dll"
    File /oname=$INSTDIR\ntdll.dll "..\Test\dll\ntdll.dll"
    File /oname=$INSTDIR\pthreadVC2.dll "..\Test\dll\pthreadVC2.dll"
    File /oname=$INSTDIR\Swmfd-connectc5.dll "..\Test\dll\Swmfd-connectc5.dll"
    File /oname=$INSTDIR\Usb4xx.dll "..\Test\dll\Usb4xx.dll"
    File /oname=$INSTDIR\VBRUN300.DLL "..\Test\dll\VBRUN300.DLL"
    File /oname=$INSTDIR\VisualReport.dll "..\Test\dll\VisualReport.dll"
    File /oname=$INSTDIR\GrFingerAppletInstaller.jar "..\Test\dll\GrFingerAppletInstaller.jar"
    File /oname=$INSTDIR\GrFingerJava.jar "..\Test\dll\GrFingerJava.jar"
    File /oname=$INSTDIR\BemaFI32.ini "..\Test\dll\BemaFI32.ini"
    File /oname=$INSTDIR\CONVERSOR.INI "..\Test\dll\CONVERSOR.INI"
    File /oname=$INSTDIR\Desktop.ini "..\Test\dll\Desktop.ini"
    File /oname=$INSTDIR\Hp12c.INI "..\Test\dll\Hp12c.INI"
    File /oname=$INSTDIR\Qrdesign.INI "..\Test\dll\Qrdesign.INI"
    File /oname=$INSTDIR\WallPaper.ini "..\Test\dll\WallPaper.ini"
	
    CreateShortCut "$DESKTOP\Test.lnk" "$INSTDIR\TestBAR.exe" "TCPIP"
    DetailPrint "Configura��o para Esta��es ..... conclu�do!"
    DetailPrint ""
SectionEnd

#----------------------------
# Instalar �cones para Servidor
Section /o "Atalhos para Servidor" SecServidor

    # Cria pasta C:\Test
    Call Test

    Exec '"$PROGRAMFILES\Sybase\SQL Anywhere 9\win32\dblang.exe" -q PT'
    File /oname=$INSTDIR\TestBAR_SENHA.exe "..\Test\TestBAR_SENHA.exe"
    File /oname=$INSTDIR\Scktsrvr.exe "..\Test\Scktsrvr.exe"
    File /oname=$INSTDIR\TestSVR.exe "..\Test\TestSVR.exe"
	
    Exec "$INSTDIR\TestSVR.exe"
    Sleep 2000
    nsExec::Exec '"taskkill" /T /F /IM TestSVR.exe'
    Sleep 2000
	
    Exec '"taskkill" /T /F /IM Scktsrvr.exe'
    Sleep 2000
    Exec '"$INSTDIR\Scktsrvr.exe"'
	
	File /oname=$INSTDIR\BemaFI32.dll "..\Test\dll\BemaFI32.dll"
	File /oname=$INSTDIR\BioNetAcsDLL.dll "..\Test\dll\BioNetAcsDLL.dll"
	File /oname=$INSTDIR\borlndmm.dll "..\Test\dll\borlndmm.dll"
	File /oname=$INSTDIR\CapPluginCertis.dll "..\Test\dll\CapPluginCertis.dll"
	File /oname=$INSTDIR\CapPluginCrossMatch.dll "..\Test\dll\CapPluginCrossMatch.dll"
	File /oname=$INSTDIR\CapPluginFingercap.dll "..\Test\dll\CapPluginFingercap.dll"
	File /oname=$INSTDIR\CapPluginHamster.dll "..\Test\dll\CapPluginHamster.dll"
	File /oname=$INSTDIR\CertisExports.dll "..\Test\dll\CertisExports.dll"
	File /oname=$INSTDIR\CONVECF95.dll "..\Test\dll\CONVECF95.dll"
	File /oname=$INSTDIR\CONVECF.dll "..\Test\dll\CONVECF.dll"
	File /oname=$INSTDIR\CONVERSOR.dll "..\Test\dll\CONVERSOR.dll"
	File /oname=$INSTDIR\DAO350.DLL "..\Test\dll\DAO350.DLL"
	File /oname=$INSTDIR\Daruma32.dll "..\Test\dll\Daruma32.dll"
	File /oname=$INSTDIR\dbxmys30.dll "..\Test\dll\dbxmys30.dll"
	File /oname=$INSTDIR\DllInscE32.dll "..\Test\dll\DllInscE32.dll"
	File /oname=$INSTDIR\dpDevClt.dll "..\Test\dll\dpDevClt.dll"
	File /oname=$INSTDIR\dpDevDat.dll "..\Test\dll\dpDevDat.dll"
	File /oname=$INSTDIR\dpFpFns.dll "..\Test\dll\dpFpFns.dll"
	File /oname=$INSTDIR\dpFtrEx.dll "..\Test\dll\dpFtrEx.dll"
	File /oname=$INSTDIR\dpMatch.dll "..\Test\dll\dpMatch.dll"
    File /oname=$INSTDIR\DLLG2.dll "..\Test\dll\DLLG2.dll"
	File /oname=$INSTDIR\Grafico.dll "..\Test\dll\Grafico.dll"
	File /oname=$INSTDIR\GrFinger.dll "..\Test\dll\GrFinger.dll"
	File /oname=$INSTDIR\GrFingerJava.dll "..\Test\dll\GrFingerJava.dll"
	File /oname=$INSTDIR\GrFingerX.dll "..\Test\dll\GrFingerX.dll"
	File /oname=$INSTDIR\Id3BiokeyDll.dll "..\Test\dll\Id3BiokeyDll.dll"
	File /oname=$INSTDIR\Imprime.dll "..\Test\dll\Imprime.dll"
	File /oname=$INSTDIR\TestRES.dll "..\Test\dll\TestRES.dll"
	File /oname=$INSTDIR\libmySQL.dll "..\Test\dll\libmySQL.dll"
	File /oname=$INSTDIR\Midas.dll "..\Test\dll\Midas.dll"
	File /oname=$INSTDIR\MP20FI32.DLL "..\Test\dll\MP20FI32.DLL"
	File /oname=$INSTDIR\NBioBSP.dll "..\Test\dll\NBioBSP.dll"
	File /oname=$INSTDIR\ntdll.dll "..\Test\dll\ntdll.dll"
	File /oname=$INSTDIR\pthreadVC2.dll "..\Test\dll\pthreadVC2.dll"
	File /oname=$INSTDIR\Swmfd-connectc5.dll "..\Test\dll\Swmfd-connectc5.dll"
	File /oname=$INSTDIR\Usb4xx.dll "..\Test\dll\Usb4xx.dll"
	File /oname=$INSTDIR\VBRUN300.DLL "..\Test\dll\VBRUN300.DLL"
	File /oname=$INSTDIR\VisualReport.dll "..\Test\dll\VisualReport.dll"
	File /oname=$INSTDIR\GrFingerAppletInstaller.jar "..\Test\dll\GrFingerAppletInstaller.jar"
	File /oname=$INSTDIR\GrFingerJava.jar "..\Test\dll\GrFingerJava.jar"
	File /oname=$INSTDIR\BemaFI32.ini "..\Test\dll\BemaFI32.ini"
	File /oname=$INSTDIR\CONVERSOR.INI "..\Test\dll\CONVERSOR.INI"
	File /oname=$INSTDIR\Desktop.ini "..\Test\dll\Desktop.ini"
	File /oname=$INSTDIR\Hp12c.INI "..\Test\dll\Hp12c.INI"
	File /oname=$INSTDIR\Qrdesign.INI "..\Test\dll\Qrdesign.INI"
	File /oname=$INSTDIR\WallPaper.ini "..\Test\dll\WallPaper.ini"

	CreateDirectory "$INSTDIR\BD\"
	#SetOverwrite off # N�o sobrep�e banco de dados
	#File /oname=$INSTDIR\BD\BDTest.DB "..\Test\Banco de Dados\BDTest.DB"
	#SetOverwrite on # Sobrep�e arquivos novamente
	
	CreateDirectory "$INSTDIR\BD\SCRIPTS\"
	CreateShortCut "$DESKTOP\BANCO DE DADOS.lnk" "$PROGRAMFILES\Sybase\SQL Anywhere 9\win32\dbsrv9.exe" "-c 256M -n BDTest $INSTDIR\BD\BDTest.DB"
	CreateShortCut "$SMSTARTUP\Borland Socket Server.lnk" "$INSTDIR\Scktsrvr.exe"
	CreateShortCut "$SMSTARTUP\BANCO DE DADOS.lnk" "$PROGRAMFILES\Sybase\SQL Anywhere 9\win32\dbsrv9.exe" "-c 256M -n BDTest $INSTDIR\BD\BDTest.DB"
    
	CreateShortCut "$DESKTOP\Test.lnk" "$INSTDIR\Test.exe" "LOCAL"
	CreateShortCut "$DESKTOP\Site Test.lnk" "$WINDIR\explorer.exe" "http://www.Test.com.br"
	
	IfFileExists $INSTDIR\BD\BDTest.DB ex1 done1
	ex1:
		ExecWait '"$PROGRAMFILES\Sybase\SQL Anywhere 9\win32\dbsrv9.exe" -f -c 256M -n BDTest $INSTDIR\BD\BDTest.DB'
		Sleep 5000 # 5 segundos para gerar o log
		Exec '"$PROGRAMFILES\Sybase\SQL Anywhere 9\win32\dbsrv9.exe" -c 256M -n BDTest $INSTDIR\BD\BDTest.DB'
		Sleep 20000 # 20 segundos para iniciar banco de dados

		# Configura o IP do Servidor no Registry
        ReadRegStr $0 HKLM "SYSTEM\CurrentControlSet\Control\ComputerName\ActiveComputerName" "ComputerName"
		StrCmp $0 "" win9x
		StrCpy $1 $0 4 3
		WriteRegStr HKCU "Software\Test" "Drive" "$0"
		Goto done2
		win9x:
			ReadRegStr $0 HKLM "SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName" "ComputerName"
			StrCpy $1 $0 4 3 
			WriteRegStr HKCU "Software\Test" "Drive" "$0"
	    done2:
			MessageBox MB_OK "IP do servidor �: \\$0 $\nAnote pois isto ser� solicitado nas esta��es."
			DetailPrint "IP do servidor configurado."
	done1:
        DetailPrint ""

	# Trazer a primeira inicializa��o com a conex�o Test
	WriteRegStr HKCU "Software\Test" "Conexao" "Test"	
	
	# Compartilhamento da pasta C:\Test
    nsExec::Exec 'net share Test=C:\Test'

	DetailPrint "Configura��o para Servidor ..... conclu�do!"
	DetailPrint ""
SectionEnd

#--------------------------------
# Descri��o dos programas
!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
!insertmacro MUI_DESCRIPTION_TEXT ${SecSybase} "Instala��o do Sybase e atualiza��es.$\n$\nOBRIGAT�RIO." 
!insertmacro MUI_DESCRIPTION_TEXT ${SecBde} "Instala��o do BDE.$\n$\nOBRIGAT�RIO."
!insertmacro MUI_DESCRIPTION_TEXT ${SecOdbc} "Configura��o do ODBC.$\n$\nOBRIGAT�RIO."
!insertmacro MUI_DESCRIPTION_TEXT ${SecInsc} "Arquivo necess�rio para verifica��o da Inscri��o estadual dos cadastros.$\n$\nOBRIGAT�RIO."
!insertmacro MUI_DESCRIPTION_TEXT ${SecEstacao} "Configura��o de atalho para esta��es. Somente selecione esta op��o se este computador for uma Esta��o de trabalho."
!insertmacro MUI_DESCRIPTION_TEXT ${SecServidor} "Configura��o para o servidor. Somente selecione esta op��o se este computador for o Servidor."
!insertmacro MUI_DESCRIPTION_TEXT ${SecData} "Configura��o do formato das datas para dd/MM/aaaa.$\n$\nOBRIGAT�RIO."
!insertmacro MUI_FUNCTION_DESCRIPTION_END
