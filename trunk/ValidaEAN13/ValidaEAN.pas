{
 * ICONE DO PROJETO TANGO DESKTOP
 * PARTE DO CODIGO FONTE DO PROJETO ACBR.SF.NET

 TODO:
 * mudar foco com enter
 * control + v no edit

 COMPATIBILIDADE:
 * D5 ATE XE2 
}

unit ValidaEAN;

interface

uses
  Windows, Messages, SysUtils, Classes, Graphics, Controls, Forms, Dialogs, StdCtrls, Math;

type
  TFValidaEAN = class(TForm)
    Label1: TLabel;
    ButtonSair: TButton;
    Label2: TLabel;
    Label3: TLabel;
    EditCodigoBarra: TEdit;
    function EAN13Valido( CodEAN13 : String ) : Boolean ;
    function EAN13_DV( CodEAN13 : String ) : String ;
    function padR(const AString : AnsiString; const nLen : Integer; const Caracter : AnsiChar = ' ') : AnsiString;
    function StrIsNumber(const S: AnsiString): Boolean;
    function CharIsNum(const C: AnsiChar): Boolean;
    function IfThen(AValue: Boolean; const ATrue: Integer; const AFalse: Integer = 0): Integer; overload;
    procedure FormShow(Sender: TObject);
    procedure ButtonSairClick(Sender: TObject);
    procedure KeyPressNumerico(var Tecla: Char);
    procedure EditCodigoBarraKeyPress(Sender: TObject; var Key: Char);
    procedure ValidaEAN;
    procedure EditCodigoBarraChange(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  FValidaEAN: TFValidaEAN;

implementation

{$R *.DFM}

procedure TFValidaEAN.KeyPressNumerico(var Tecla: Char);
begin
   if Tecla <> #8 then
   begin
      if not (Tecla in ['0'..'9']) then
      begin
         Tecla := #0;
      end;
   end;
end;

function TFValidaEAN.IfThen(AValue: Boolean; const ATrue: Integer; const AFalse: Integer): Integer;
begin
  if AValue then
    Result := ATrue
  else Result := AFalse;
end;

function TFValidaEAN.CharIsNum(const C: AnsiChar): Boolean;
begin
  Result := ( C in ['0'..'9'] ) ;
end ;

function TFValidaEAN.StrIsNumber(const S: AnsiString): Boolean;
Var
  A, LenStr : Integer ;
begin
  LenStr := Length( S ) ;
  Result := (LenStr > 0) ;
  A      := 1 ;
  while Result and ( A <= LenStr )  do
  begin
     Result := CharIsNum( S[A] ) ;
     Inc(A) ;
  end;
end ;

function TFValidaEAN.padR(const AString : AnsiString; const nLen : Integer;
   const Caracter : AnsiChar) : AnsiString ;
var
  Tam: Integer;
begin
  Tam := Length(AString);
  if Tam < nLen then
    Result := StringOfChar(Caracter, (nLen - Tam)) + AString
  else
    Result := copy(AString,1,nLen) ;
end ;

function TFValidaEAN.EAN13_DV(CodEAN13: String): String;
Var A,DV : Integer ;
begin
   Result   := '' ;
   CodEAN13 := PadR(Trim(CodEAN13),12,'0') ;
   if not StrIsNumber( CodEAN13 ) then
      exit ;

   DV := 0;
   For A := 12 downto 1 do
      DV := DV + (StrToInt( CodEAN13[A] ) * IfThen(odd(A),1,3));

   DV := (Ceil( DV / 10 ) * 10) - DV ;

   Result := IntToStr( DV );
end;

function TFValidaEAN.EAN13Valido(CodEAN13: String): Boolean;
begin
  Result := false ;
  if Length(CodEAN13) = 13 then
     Result := ( CodEAN13[13] =  EAN13_DV(CodEAN13) ) ;
end;

procedure TFValidaEAN.FormShow(Sender: TObject);
begin
   Label1.Caption := 'Digite um código de 13 dígitos';
   Label1.Font.Color := clBlack;
   Label2.Caption := '0';
end;

procedure TFValidaEAN.ButtonSairClick(Sender: TObject);
begin
   Close;
end;

procedure TFValidaEAN.EditCodigoBarraKeyPress(Sender: TObject; var Key: Char);
begin
   KeyPressNumerico(Key);
end;

procedure TFValidaEAN.ValidaEAN;
begin
   if EAN13Valido(EditCodigoBarra.Text) then
   begin
      Label1.Caption := 'Código de barras válido!';
      Label1.Font.Color := clGreen;
   end
   else
   begin
      Label1.Caption := 'Código de barras NÃO é válido!';
      Label1.Font.Color := clRed;
   end;

   if (EditCodigoBarra.Text = '') then
   begin
      Label1.Caption := 'Digite um código de 13 dígitos';
      Label1.Font.Color := clBlack;
   end;
   Label2.Caption := inttostr(length(EditCodigoBarra.Text));
end;

procedure TFValidaEAN.EditCodigoBarraChange(Sender: TObject);
begin
   ValidaEAN;
end;

end.
