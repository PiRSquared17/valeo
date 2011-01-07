unit main;

interface

uses
{$IFNDEF VER130BELOW}
  Types,
{$ENDIF}
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, DB, ZAbstractRODataset, ZAbstractDataset, ZDataset, ZConnection,
  StdCtrls, ExtCtrls, Buttons, ComCtrls, Grids, DBGrids, Mask, DBCtrls,
  ExtDlgs, ZSqlMetadata, ZSqlMonitor, ZDbcLogging, Menus;

type
  TMainForm = class(TForm)
    ZConnection: TZConnection;
    ZSQLMetadata: TZSQLMetadata;
    DSSQLMetadata: TDataSource;
    ZSQLMonitor: TZSQLMonitor;
    MainMenu1: TMainMenu;
    Cadastros1: TMenuItem;
    Supermercado1: TMenuItem;
    Marca1: TMenuItem;
    Unidade1: TMenuItem;
    Produtos1: TMenuItem;
    N1: TMenuItem;
    Usurios1: TMenuItem;
    Lanamentos1: TMenuItem;
    Compra1: TMenuItem;
    Relatrios1: TMenuItem;
    Sair1: TMenuItem;
    BitBtnSair: TBitBtn;
    SBCompra: TSpeedButton;
    SBProduto: TSpeedButton;
    SBMercado: TSpeedButton;
    procedure FormCreate(Sender: TObject);
    procedure BitBtnSairClick(Sender: TObject);
    procedure SBMercadoClick(Sender: TObject);
  private
    { Private declarations }
    procedure DoEnterAsTab(var Msg: TMsg; var Handled: Boolean);
  public
    { Public declarations }
  end;

var
  MainForm: TMainForm;

implementation

{$R *.dfm}

uses ZClasses, ZDbcIntfs, ZDbcDBLib, ZCompatibility, FMercado;

procedure TMainForm.DoEnterAsTab(var Msg: TMsg; var Handled: Boolean);
begin
  if Msg.Message = WM_KEYDOWN then
  if Msg.wParam = VK_RETURN then Keybd_event(VK_TAB, 0, 0, 0);
end;

procedure TMainForm.BitBtnSairClick(Sender: TObject);
begin
   ZConnection.Disconnect;
   Close;
end;

procedure TMainForm.FormCreate(Sender: TObject);
begin
    Application.OnMessage := DoEnterAsTab;
    try
       ZConnection.Connected;
       Height := 179;
    except
       ShowMessage('Não foi possível conectar com o banco de dados!');
       Application.Terminate;
    end;
end;

procedure TMainForm.SBMercadoClick(Sender: TObject);
begin
   Application.CreateForm(TFormMercado, FormMercado);
   try
      FormMercado.ShowModal;
   finally
      FormMercado.Free;
   end;
end;

end.
