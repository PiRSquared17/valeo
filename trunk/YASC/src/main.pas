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
    ZSupermercado: TZQuery;
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
    SpeedButton1: TSpeedButton;
    SpeedButton2: TSpeedButton;
    SpeedButton3: TSpeedButton;
    procedure BitBtnSairClick(Sender: TObject);
    procedure FormCreate(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  MainForm: TMainForm;

implementation

{$R *.dfm}

uses ZClasses, ZDbcIntfs, ZDbcDBLib, ZCompatibility;

procedure TMainForm.BitBtnSairClick(Sender: TObject);
begin
   if MessageDlg('Deseja realmente sair do sistema?', mtinformation, [mbyes,mbno],0) = mryes then
   begin
      ZConnection.Disconnect;
      Close;
   end;
end;


procedure TMainForm.FormCreate(Sender: TObject);
begin
    try
       ZConnection.Connected;
       Height := 179;
    except
       ShowMessage('Não foi possível conectar com o banco de dados!');
       Application.Terminate;
    end;
end;

end.
