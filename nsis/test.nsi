/*
Intelecto Tecnologia e Sistemas
Instalador dos Sistemas Intesig
*/

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

Function "Intesig"
	CreateDirectory "$INSTDIR"
FunctionEnd

#--------------------------------
# Privilégios de usuário para instalação do INTESIG no Windows Vista
RequestExecutionLevel admin

XPStyle on
Name "INTESIG"
OutFile "INTESIG.exe"
InstallDir "C:\INTESIG"

#--------------------------------
# Texto do rodapé
BrandingText "Intelecto Tecnologia e Sistemas"

#--------------------------------
# Logotipo no topo
!define MUI_HEADERIMAGE
!define MUI_HEADERIMAGE_BITMAP "..\INTESIG\Imagens\intesig.bmp"
!define MUI_ICON "..\INTESIG\Imagens\icone.ico"
!define MUI_WELCOMEFINISHPAGE_BITMAP "..\INTESIG\Imagens\intelecto.bmp"
!define MUI_FINISHPAGE_NOAUTOCLOSE

#--------------------------------
# Páginas
Page custom nsDialogsWelcome
#!insertmacro MUI_PAGE_DIRECTORY # Escolha do diretório de instalação do Intesig, padrão C:\INTESIG
!insertmacro MUI_PAGE_COMPONENTS
!insertmacro MUI_PAGE_INSTFILES

#--------------------------------
# Definição língua
!insertmacro MUI_LANGUAGE "PortugueseBR"

# Verifica se já foi aberto janela de instalação
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
    MessageBox MB_OK|MB_ICONEXCLAMATION "O INTESIG já está sendo instalado neste computador!"
    Abort
    CreateFont $HEADLINE_FONT "$(^Font)" "14" "500"
    InitPluginsDir
    File /oname=$TEMP\intelecto.bmp "..\INTESIG\Imagens\intelecto.bmp"
  
FunctionEnd

#--------------------------------
# Esconder controles da tela de início
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
# Texto da tela de início
Function nsDialogsWelcome

    nsDialogs::Create 1044
    Pop $DIALOG

    nsDialogs::CreateControl STATIC ${WS_VISIBLE}|${WS_CHILD}|${WS_CLIPSIBLINGS}|${SS_BITMAP} 0 0 0 109u 193u ""
    Pop $IMAGECTL

    StrCpy $0 "..\INTESIG\Imagens\intelecto.bmp"
    System::Call 'user32::LoadImage(i 0, t r0, i ${IMAGE_BITMAP}, i 0, i 0, i ${LR_LOADFROMFILE}) i.s'
    Pop $IMAGE
	
    SendMessage $IMAGECTL ${STM_SETIMAGE} ${IMAGE_BITMAP} $IMAGE

    nsDialogs::CreateControl STATIC ${WS_VISIBLE}|${WS_CHILD}|${WS_CLIPSIBLINGS} 0 115u 5u -130u 20u "IMPORTANTE !!!"
    Pop $HEADLINE

    CreateFont $1 "Verdana" "18" "650" /UNDERLINE
    SendMessage $HEADLINE ${WM_SETFONT} $1 1

    nsDialogs::CreateControl STATIC ${WS_VISIBLE}|${WS_CHILD}|${WS_CLIPSIBLINGS} 0 115u 25u -130u -20u "$\r$\nDepois de instalado o sistema, a primeira vez que iniciar o INTESIG tem que ser pelo servidor. Digite o usuário, senha e logo depois aparecerá a tela de liberação do sistema, anote a data de validade, o número do contrato e o número da identificação e em seguida entre em contato com o setor administrativo da Intelecto pelo telefone (65) 3314-3300 repassando as informações para obter a senha de liberação do sistema.$\r$\n$\r$\nDepois de obtido a liberação, é necessário acessar o site da Intelecto, entrar na opção Portal do Cliente, fornecer o número do contrato e senha e fazer o download dos módulos habilitados para sua empresa.$\r$\n$\r$\n Intelecto Tecnologia e Sistemas $\n www.intelecto.com.br $\n E-mail: atendimento@intelecto.com.br $\n Suporte Técnico (65) 3314-3300"
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

# Sobrepõe arquivos já existentes
SetOverwrite on 
# Não mostrar mensagens do progresso da instalação para não ficar visível a senha de dba
ShowInstDetails nevershow 

#----------------------------
# Sybase
Section "Sybase" SecSybase
	
    DetailPrint "Instalando o Sybase, aguarde....."
    MessageBox MB_OK 'Na próxima tela, escolha o país "Brazil", marque a opção "I accept" em seguida clique sobre o botão "Next".$\r$\n'

    ExecWait '..\INTESIG\Sybase\setup.exe'
	
    DetailPrint "Instalação do Sybase .....concluído!"

    DetailPrint "Instalando a 1ª atualização do Sybase, aguarde....."
    ExecWait '..\INTESIG\Atualização1\setup.exe'
    DetailPrint "Instalação da 1ª atualização do Sybase .....concluído!"
    DetailPrint ""

    DetailPrint "Instalando a 2ª atualização do Sybase, aguarde....."
    ExecWait '..\INTESIG\Atualização2\setup.exe'
    DetailPrint "Instalação da 2ª atualização do Sybase .....concluído!"
    DetailPrint ""
SectionEnd

#----------------------------
# ODBC
Section "Configuração do ODBC" SecOdbc
    WriteRegStr HKLM "Software\ODBC\ODBC.INI\ODBC Data Sources" "INTESIG" "Adaptive Server Anywhere 9.0"
    WriteRegStr HKLM "Software\ODBC\ODBC.INI\INTESIG" "Driver" "$PROGRAMFILES\Sybase\SQL Anywhere 9\win32\dbodbc9.dll"
    WriteRegStr HKLM "Software\ODBC\ODBC.INI\INTESIG" "EngineName" "BDINTESIG"
    WriteRegStr HKLM "Software\ODBC\ODBC.INI\INTESIG" "AutoStop" "Yes"
    WriteRegStr HKLM "Software\ODBC\ODBC.INI\INTESIG" "Integrated" "No"
    WriteRegStr HKLM "Software\ODBC\ODBC.INI\INTESIG" "Debug" "No"
    WriteRegStr HKLM "Software\ODBC\ODBC.INI\INTESIG" "DisableMultiRowFetch" "No"
    WriteRegStr HKLM "Software\ODBC\ODBC.INI\INTESIG" "CommLinks" "SharedMemory,TCPIP{}"
    WriteRegStr HKLM "Software\ODBC\ODBC.INI\INTESIG" "Compress" "No"
    WriteRegStr HKLM "Software\ODBC\ODBC.INI\INTESIG" "Delphi" "Yes"
    WriteRegStr HKLM "Software\Borland\Database Engine\Settings\DRIVERS\SYBASE\DB OPEN" "TDS PACKET SIZE" "8192"
    DetailPrint "Configuração do ODBC .....concluído!"
    DetailPrint ""
SectionEnd

#----------------------------
# BDE
Section "BDE" SecBde
    DetailPrint "Instalando o BDE, aguarde....."
    ExecWait '..\INTESIG\BDE\SETUP.EXE'
    Sleep 15000 # 15 segundos para instalar BDE
    CreateDirectory "$PROGRAMFILES\Borland\Common Files\BDE\"
    File "/oname=$PROGRAMFILES\Borland\Common Files\BDE\IDAPI.CFG" ..\INTESIG\BDE\IDAPI.CFG
    File "/oname=$PROGRAMFILES\Borland\Common Files\BDE\IDAPI32.CFG" ..\INTESIG\BDE\IDAPI32.CFG
    DetailPrint "Instalação do BDE .....concluído!"
    DetailPrint ""
SectionEnd

#----------------------------
# Configuração do formato de Data
Section "Configuração de Data" SecData
    WriteRegStr HKCU "Control Panel\International" "sShortDate" "dd/MM/yyyy"
    WriteRegStr HKU ".DEFAULT\Control Panel\International" "sShortDate" "dd/MM/yyyy"
    WriteRegStr HKU "S-1-5-18\Control Panel\International" "sShortDate" "dd/MM/yyyy"
    WriteRegStr HKU "S-1-5-19\Control Panel\International" "sShortDate" "dd/MM/yyyy"
    WriteRegStr HKU "S-1-5-20\Control Panel\International" "sShortDate" "dd/MM/yyyy"
    DetailPrint "Configuração do formato de data .....concluído!"
    DetailPrint ""
SectionEnd

#----------------------------
# DllInsc32 na pasta system32

Section "DllInscE32.dll" SecInsc
    File /oname=$SYSDIR\DllInscE32.dll "..\INTESIG\dll\DllInscE32.dll"
    DetailPrint "Instalação da DllInsc32 ..... concluído!"
    DetailPrint ""
SectionEnd

#----------------------------
# Criando atalho do Intesig para estações
Section "Atalhos para Estação" SecEstacao

    # Cria pasta C:\INTESIG
    Call Intesig

    Exec '"$PROGRAMFILES\Sybase\SQL Anywhere 9\win32\dblang.exe" -q PT'
    File /oname=$INSTDIR\IntesigBAR_SENHA.exe "..\INTESIG\Executáveis\IntesigBAR_SENHA.exe"

    File /oname=$INSTDIR\BemaFI32.dll "..\INTESIG\dll\BemaFI32.dll"
    File /oname=$INSTDIR\BioNetAcsDLL.dll "..\INTESIG\dll\BioNetAcsDLL.dll"
    File /oname=$INSTDIR\borlndmm.dll "..\INTESIG\dll\borlndmm.dll"
    File /oname=$INSTDIR\CapPluginCertis.dll "..\INTESIG\dll\CapPluginCertis.dll"
    File /oname=$INSTDIR\CapPluginCrossMatch.dll "..\INTESIG\dll\CapPluginCrossMatch.dll"
    File /oname=$INSTDIR\CapPluginFingercap.dll "..\INTESIG\dll\CapPluginFingercap.dll"
    File /oname=$INSTDIR\CapPluginHamster.dll "..\INTESIG\dll\CapPluginHamster.dll"
    File /oname=$INSTDIR\CertisExports.dll "..\INTESIG\dll\CertisExports.dll"
    File /oname=$INSTDIR\CONVECF95.dll "..\INTESIG\dll\CONVECF95.dll"
    File /oname=$INSTDIR\CONVECF.dll "..\INTESIG\dll\CONVECF.dll"
    File /oname=$INSTDIR\CONVERSOR.dll "..\INTESIG\dll\CONVERSOR.dll"
    File /oname=$INSTDIR\DAO350.DLL "..\INTESIG\dll\DAO350.DLL"
    File /oname=$INSTDIR\Daruma32.dll "..\INTESIG\dll\Daruma32.dll"
    File /oname=$INSTDIR\DLLG2.dll "..\INTESIG\dll\DLLG2.dll"
    File /oname=$INSTDIR\dbxmys30.dll "..\INTESIG\dll\dbxmys30.dll"
    File /oname=$INSTDIR\DllInscE32.dll "..\INTESIG\dll\DllInscE32.dll"
    File /oname=$INSTDIR\dpDevClt.dll "..\INTESIG\dll\dpDevClt.dll"
    File /oname=$INSTDIR\dpDevDat.dll "..\INTESIG\dll\dpDevDat.dll"
    File /oname=$INSTDIR\dpFpFns.dll "..\INTESIG\dll\dpFpFns.dll"
    File /oname=$INSTDIR\dpFtrEx.dll "..\INTESIG\dll\dpFtrEx.dll"
    File /oname=$INSTDIR\dpMatch.dll "..\INTESIG\dll\dpMatch.dll"
    File /oname=$INSTDIR\Grafico.dll "..\INTESIG\dll\Grafico.dll"
    File /oname=$INSTDIR\GrFinger.dll "..\INTESIG\dll\GrFinger.dll"
    File /oname=$INSTDIR\GrFingerJava.dll "..\INTESIG\dll\GrFingerJava.dll"
    File /oname=$INSTDIR\GrFingerX.dll "..\INTESIG\dll\GrFingerX.dll"
    File /oname=$INSTDIR\Id3BiokeyDll.dll "..\INTESIG\dll\Id3BiokeyDll.dll"
    File /oname=$INSTDIR\Imprime.dll "..\INTESIG\dll\Imprime.dll"
    File /oname=$INSTDIR\IntesigRES.dll "..\INTESIG\dll\IntesigRES.dll"
    File /oname=$INSTDIR\libmySQL.dll "..\INTESIG\dll\libmySQL.dll"
    File /oname=$INSTDIR\Midas.dll "..\INTESIG\dll\Midas.dll"
    File /oname=$INSTDIR\MP20FI32.DLL "..\INTESIG\dll\MP20FI32.DLL"
    File /oname=$INSTDIR\NBioBSP.dll "..\INTESIG\dll\NBioBSP.dll"
    File /oname=$INSTDIR\ntdll.dll "..\INTESIG\dll\ntdll.dll"
    File /oname=$INSTDIR\pthreadVC2.dll "..\INTESIG\dll\pthreadVC2.dll"
    File /oname=$INSTDIR\Swmfd-connectc5.dll "..\INTESIG\dll\Swmfd-connectc5.dll"
    File /oname=$INSTDIR\Usb4xx.dll "..\INTESIG\dll\Usb4xx.dll"
    File /oname=$INSTDIR\VBRUN300.DLL "..\INTESIG\dll\VBRUN300.DLL"
    File /oname=$INSTDIR\VisualReport.dll "..\INTESIG\dll\VisualReport.dll"
    File /oname=$INSTDIR\GrFingerAppletInstaller.jar "..\INTESIG\dll\GrFingerAppletInstaller.jar"
    File /oname=$INSTDIR\GrFingerJava.jar "..\INTESIG\dll\GrFingerJava.jar"
    File /oname=$INSTDIR\BemaFI32.ini "..\INTESIG\dll\BemaFI32.ini"
    File /oname=$INSTDIR\CONVERSOR.INI "..\INTESIG\dll\CONVERSOR.INI"
    File /oname=$INSTDIR\Desktop.ini "..\INTESIG\dll\Desktop.ini"
    File /oname=$INSTDIR\Hp12c.INI "..\INTESIG\dll\Hp12c.INI"
    File /oname=$INSTDIR\Qrdesign.INI "..\INTESIG\dll\Qrdesign.INI"
    File /oname=$INSTDIR\WallPaper.ini "..\INTESIG\dll\WallPaper.ini"
	
    CreateShortCut "$DESKTOP\INTESIG.lnk" "$INSTDIR\IntesigBAR.exe" "TCPIP"
    DetailPrint "Configuração para Estações ..... concluído!"
    DetailPrint ""
SectionEnd

#----------------------------
# Instalar ícones para Servidor
Section /o "Atalhos para Servidor" SecServidor

    # Cria pasta C:\INTESIG
    Call Intesig

    Exec '"$PROGRAMFILES\Sybase\SQL Anywhere 9\win32\dblang.exe" -q PT'
    File /oname=$INSTDIR\IntesigBAR_SENHA.exe "..\INTESIG\Executáveis\IntesigBAR_SENHA.exe"
    File /oname=$INSTDIR\Scktsrvr.exe "..\INTESIG\Executáveis\Scktsrvr.exe"
    File /oname=$INSTDIR\INTESIGSVR.exe "..\INTESIG\Executáveis\INTESIGSVR.exe"
	
    Exec "$INSTDIR\INTESIGSVR.exe"
    Sleep 2000
    nsExec::Exec '"taskkill" /T /F /IM INTESIGSVR.exe'
    Sleep 2000
	
    Exec '"taskkill" /T /F /IM Scktsrvr.exe'
    Sleep 2000
    Exec '"$INSTDIR\Scktsrvr.exe"'
	
	File /oname=$INSTDIR\BemaFI32.dll "..\INTESIG\dll\BemaFI32.dll"
	File /oname=$INSTDIR\BioNetAcsDLL.dll "..\INTESIG\dll\BioNetAcsDLL.dll"
	File /oname=$INSTDIR\borlndmm.dll "..\INTESIG\dll\borlndmm.dll"
	File /oname=$INSTDIR\CapPluginCertis.dll "..\INTESIG\dll\CapPluginCertis.dll"
	File /oname=$INSTDIR\CapPluginCrossMatch.dll "..\INTESIG\dll\CapPluginCrossMatch.dll"
	File /oname=$INSTDIR\CapPluginFingercap.dll "..\INTESIG\dll\CapPluginFingercap.dll"
	File /oname=$INSTDIR\CapPluginHamster.dll "..\INTESIG\dll\CapPluginHamster.dll"
	File /oname=$INSTDIR\CertisExports.dll "..\INTESIG\dll\CertisExports.dll"
	File /oname=$INSTDIR\CONVECF95.dll "..\INTESIG\dll\CONVECF95.dll"
	File /oname=$INSTDIR\CONVECF.dll "..\INTESIG\dll\CONVECF.dll"
	File /oname=$INSTDIR\CONVERSOR.dll "..\INTESIG\dll\CONVERSOR.dll"
	File /oname=$INSTDIR\DAO350.DLL "..\INTESIG\dll\DAO350.DLL"
	File /oname=$INSTDIR\Daruma32.dll "..\INTESIG\dll\Daruma32.dll"
	File /oname=$INSTDIR\dbxmys30.dll "..\INTESIG\dll\dbxmys30.dll"
	File /oname=$INSTDIR\DllInscE32.dll "..\INTESIG\dll\DllInscE32.dll"
	File /oname=$INSTDIR\dpDevClt.dll "..\INTESIG\dll\dpDevClt.dll"
	File /oname=$INSTDIR\dpDevDat.dll "..\INTESIG\dll\dpDevDat.dll"
	File /oname=$INSTDIR\dpFpFns.dll "..\INTESIG\dll\dpFpFns.dll"
	File /oname=$INSTDIR\dpFtrEx.dll "..\INTESIG\dll\dpFtrEx.dll"
	File /oname=$INSTDIR\dpMatch.dll "..\INTESIG\dll\dpMatch.dll"
    File /oname=$INSTDIR\DLLG2.dll "..\INTESIG\dll\DLLG2.dll"
	File /oname=$INSTDIR\Grafico.dll "..\INTESIG\dll\Grafico.dll"
	File /oname=$INSTDIR\GrFinger.dll "..\INTESIG\dll\GrFinger.dll"
	File /oname=$INSTDIR\GrFingerJava.dll "..\INTESIG\dll\GrFingerJava.dll"
	File /oname=$INSTDIR\GrFingerX.dll "..\INTESIG\dll\GrFingerX.dll"
	File /oname=$INSTDIR\Id3BiokeyDll.dll "..\INTESIG\dll\Id3BiokeyDll.dll"
	File /oname=$INSTDIR\Imprime.dll "..\INTESIG\dll\Imprime.dll"
	File /oname=$INSTDIR\IntesigRES.dll "..\INTESIG\dll\IntesigRES.dll"
	File /oname=$INSTDIR\libmySQL.dll "..\INTESIG\dll\libmySQL.dll"
	File /oname=$INSTDIR\Midas.dll "..\INTESIG\dll\Midas.dll"
	File /oname=$INSTDIR\MP20FI32.DLL "..\INTESIG\dll\MP20FI32.DLL"
	File /oname=$INSTDIR\NBioBSP.dll "..\INTESIG\dll\NBioBSP.dll"
	File /oname=$INSTDIR\ntdll.dll "..\INTESIG\dll\ntdll.dll"
	File /oname=$INSTDIR\pthreadVC2.dll "..\INTESIG\dll\pthreadVC2.dll"
	File /oname=$INSTDIR\Swmfd-connectc5.dll "..\INTESIG\dll\Swmfd-connectc5.dll"
	File /oname=$INSTDIR\Usb4xx.dll "..\INTESIG\dll\Usb4xx.dll"
	File /oname=$INSTDIR\VBRUN300.DLL "..\INTESIG\dll\VBRUN300.DLL"
	File /oname=$INSTDIR\VisualReport.dll "..\INTESIG\dll\VisualReport.dll"
	File /oname=$INSTDIR\GrFingerAppletInstaller.jar "..\INTESIG\dll\GrFingerAppletInstaller.jar"
	File /oname=$INSTDIR\GrFingerJava.jar "..\INTESIG\dll\GrFingerJava.jar"
	File /oname=$INSTDIR\BemaFI32.ini "..\INTESIG\dll\BemaFI32.ini"
	File /oname=$INSTDIR\CONVERSOR.INI "..\INTESIG\dll\CONVERSOR.INI"
	File /oname=$INSTDIR\Desktop.ini "..\INTESIG\dll\Desktop.ini"
	File /oname=$INSTDIR\Hp12c.INI "..\INTESIG\dll\Hp12c.INI"
	File /oname=$INSTDIR\Qrdesign.INI "..\INTESIG\dll\Qrdesign.INI"
	File /oname=$INSTDIR\WallPaper.ini "..\INTESIG\dll\WallPaper.ini"

	CreateDirectory "$INSTDIR\BD\"
	#SetOverwrite off # Não sobrepõe banco de dados
	#File /oname=$INSTDIR\BD\BDINTESIG.DB "..\INTESIG\Banco de Dados\BDINTESIG.DB"
	#SetOverwrite on # Sobrepõe arquivos novamente
	
	CreateDirectory "$INSTDIR\BD\SCRIPTS\"
	CreateShortCut "$DESKTOP\BANCO DE DADOS.lnk" "$PROGRAMFILES\Sybase\SQL Anywhere 9\win32\dbsrv9.exe" "-c 256M -n BDINTESIG $INSTDIR\BD\BDINTESIG.DB"
	CreateShortCut "$SMSTARTUP\Borland Socket Server.lnk" "$INSTDIR\Scktsrvr.exe"
	CreateShortCut "$SMSTARTUP\BANCO DE DADOS.lnk" "$PROGRAMFILES\Sybase\SQL Anywhere 9\win32\dbsrv9.exe" "-c 256M -n BDINTESIG $INSTDIR\BD\BDINTESIG.DB"
    
	CreateShortCut "$DESKTOP\INTESIG.lnk" "$INSTDIR\IntesigBAR_SENHA.exe" "LOCAL"
	CreateShortCut "$DESKTOP\Site Intelecto.lnk" "$WINDIR\explorer.exe" "http://www.intelecto.com.br"
	
	IfFileExists $INSTDIR\BD\BDINTESIG.DB ex1 done1
	ex1:
		ExecWait '"$PROGRAMFILES\Sybase\SQL Anywhere 9\win32\dbsrv9.exe" -f -c 256M -n BDINTESIG $INSTDIR\BD\BDINTESIG.DB'
		Sleep 5000 # 5 segundos para gerar o log
		Exec '"$PROGRAMFILES\Sybase\SQL Anywhere 9\win32\dbsrv9.exe" -c 256M -n BDINTESIG $INSTDIR\BD\BDINTESIG.DB'
		Sleep 20000 # 20 segundos para iniciar banco de dados

		# Configura o IP do Servidor no Registry
        ReadRegStr $0 HKLM "SYSTEM\CurrentControlSet\Control\ComputerName\ActiveComputerName" "ComputerName"
		StrCmp $0 "" win9x
		StrCpy $1 $0 4 3
		WriteRegStr HKCU "Software\Intesig" "Drive" "$0"
		Goto done2
		win9x:
			ReadRegStr $0 HKLM "SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName" "ComputerName"
			StrCpy $1 $0 4 3 
			WriteRegStr HKCU "Software\Intesig" "Drive" "$0"
	    done2:
			MessageBox MB_OK "IP do servidor é: \\$0 $\nAnote pois isto será solicitado nas estações."
			DetailPrint "IP do servidor configurado."
	done1:
        DetailPrint ""

	# Trazer a primeira inicialização com a conexão INTESIG
	WriteRegStr HKCU "Software\Intesig" "Conexao" "INTESIG"	
	
	# Compartilhamento da pasta C:\INTESIG
    nsExec::Exec 'net share INTESIG=C:\INTESIG'

	DetailPrint "Configuração para Servidor ..... concluído!"
	DetailPrint ""
SectionEnd

#--------------------------------
# Descrição dos programas
!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
!insertmacro MUI_DESCRIPTION_TEXT ${SecSybase} "Instalação do Sybase e atualizações.$\n$\nOBRIGATÓRIO." 
!insertmacro MUI_DESCRIPTION_TEXT ${SecBde} "Instalação do BDE.$\n$\nOBRIGATÓRIO."
!insertmacro MUI_DESCRIPTION_TEXT ${SecOdbc} "Configuração do ODBC.$\n$\nOBRIGATÓRIO."
!insertmacro MUI_DESCRIPTION_TEXT ${SecInsc} "Arquivo necessário para verificação da Inscrição estadual dos cadastros.$\n$\nOBRIGATÓRIO."
!insertmacro MUI_DESCRIPTION_TEXT ${SecEstacao} "Configuração de atalho para estações. Somente selecione esta opção se este computador for uma Estação de trabalho."
!insertmacro MUI_DESCRIPTION_TEXT ${SecServidor} "Configuração para o servidor. Somente selecione esta opção se este computador for o Servidor."
!insertmacro MUI_DESCRIPTION_TEXT ${SecData} "Configuração do formato das datas para dd/MM/aaaa.$\n$\nOBRIGATÓRIO."
!insertmacro MUI_FUNCTION_DESCRIPTION_END
