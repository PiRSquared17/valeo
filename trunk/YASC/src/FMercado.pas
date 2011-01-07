unit FMercado;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, Buttons, DB, ZAbstractRODataset, ZAbstractDataset, ZDataset,
  ZConnection;

type
  TFormMercado = class(TForm)
    EditCodigo: TEdit;
    BitBtnConfirmar: TBitBtn;
    BitBtnExcluir: TBitBtn;
    BitBtnSair: TBitBtn;
    LbCodigo: TLabel;
    LbDescricao: TLabel;
    EditDescricao: TEdit;
    ZMercado: TZQuery;
    ZConnection: TZConnection;
    procedure BitBtnConfirmarClick(Sender: TObject);
    procedure BitBtnSairClick(Sender: TObject);
    procedure BitBtnExcluirClick(Sender: TObject);
    procedure EditCodigoEnter(Sender: TObject);
    procedure FormShow(Sender: TObject);
    procedure EditCodigoExit(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  FormMercado: TFormMercado;

implementation

var
   Codigo: integer;

{$R *.dfm}

procedure TFormMercado.FormShow(Sender: TObject);
begin
   EditCodigoEnter(Sender);
end;

procedure TFormMercado.BitBtnSairClick(Sender: TObject);
begin
   Close;
end;

procedure TFormMercado.EditCodigoEnter(Sender: TObject);
begin
   with ZMercado do
   begin
      Close;
      Sql.Clear;
      Sql.Add('Select coalesce(max(codigo_merc),0)+1 as CODIGO from tbmercado');
      Open;
      EditCodigo.Text := IntToStr(FieldByName('CODIGO').AsInteger);
      EditDescricao.Text := '';
   end;
   EditCodigo.SetFocus;
   EditCodigo.SelectAll;
end;

procedure TFormMercado.EditCodigoExit(Sender: TObject);
begin
   with ZMercado do
   begin
      Close;
      sql.clear;
      Sql.Add('SELECT * FROM TBMERCADO WHERE CODIGO_MERC = :CODIGO_MERC');
      ParamByName('CODIGO_MERC').AsString := EditCodigo.Text;
      Open;
      Codigo := (fieldByName('CODIGO_MERC').AsInteger);
      If IsEmpty then
      begin
         EditDescricao.Text := '';
      end
      else
      begin
          EditDescricao.Text := FieldByName('DESCRICAO_MERC').asString;
      end;
   end;
end;

procedure TFormMercado.BitBtnConfirmarClick(Sender: TObject);
begin
   if (EditCodigo.Text='') or (EditDescricao.Text='') then
      ShowMessage ('Descrição não incluída!') else
   with ZMercado do
   begin
      if (EditCodigo.Text) <> IntToStr(Codigo) then
      begin
         Close;
         Sql.Clear;
         Sql.Add('INSERT INTO TBMERCADO (CODIGO_MERC, DESCRICAO_MERC) ');
         Sql.Add('VALUES (:CODIGO_MERC, :DESCRICAO_MERC);');
      end
      else
      begin
         Close;
         Sql.Clear;
         Sql.Add('UPDATE TBMERCADO SET ');
         Sql.Add('DESCRICAO_MERC =:DESCRICAO_MERC ');
         Sql.Add('WHERE CODIGO_MERC = :CODIGO_MERC;');
      end;
      ParamByname('CODIGO_MERC').AsInteger   := StrToInt(EditCodigo.Text);
      ParamByname('DESCRICAO_MERC').AsString := EditDescricao.Text;
      ExecSQL;
      ShowMessage ('Supermercado incluído com sucesso!');
   end;
   EditCodigoEnter(Sender);
end;

procedure TFormMercado.BitBtnExcluirClick(Sender: TObject);
begin
   with ZMercado do
   begin
      if (EditCodigo.Text) = IntToStr(Codigo) then
      begin
         if MessageDlg('Tem certeza que deseja excluir este cadastro?', mtinformation, [mbYes, mbNo], 0) = mryes then
         begin
            Close;
            Sql.Clear;
            Sql.Add('DELETE FROM TBMERCADO WHERE CODIGO_MERC = :CODIGO_MERC;');
            ParamByname('CODIGO_MERC').AsInteger   := StrToInt(EditCodigo.Text);
            ExecSQL;
            ShowMessage ('Código de Supermercado excluído com sucesso!');
         end;
      end;
   end;
   EditCodigoEnter(Sender);
end;

end.
