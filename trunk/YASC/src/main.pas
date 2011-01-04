unit main;

interface

uses
{$IFNDEF VER130BELOW}
  Types,
{$ENDIF}
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, DB, ZAbstractRODataset, ZAbstractDataset, ZDataset, ZConnection,
  StdCtrls, ExtCtrls, Buttons, ComCtrls, Grids, DBGrids, Mask, DBCtrls,
  ExtDlgs, ZSqlMetadata, ZSqlMonitor, ZDbcLogging;

type
  TMainForm = class(TForm)
    ZConnection: TZConnection;
    ZSupermercado: TZQuery;
    ZSQLMetadata: TZSQLMetadata;
    DSSQLMetadata: TDataSource;
    ZSQLMonitor: TZSQLMonitor;
    BitBtnSair: TBitBtn;
    ZSupermercadocodigo: TIntegerField;
    ZSupermercadodescricao: TWideStringField;
    procedure BitBtnSairClick(Sender: TObject);
    procedure FormShow(Sender: TObject);
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
   ZConnection.Disconnect;
   Close;
end;

procedure TMainForm.FormShow(Sender: TObject);
begin
  with ZConnection do
  begin
    try
       Connect;
       ZSupermercado.Active := True;
    except
       ShowMessage('Não foi possível conectar com o banco de dados!');
       Application.Terminate;
    end;
  end;
end;

end.
