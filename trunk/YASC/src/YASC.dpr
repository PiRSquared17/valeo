program YASC;

uses
  Forms,
  main in 'main.pas' {MainForm},
  FMercado in 'FMercado.pas' {FormMercado};

{$R *.res}

begin
  Application.Initialize;
  Application.Title := 'YASC';
  Application.CreateForm(TMainForm, MainForm);
  Application.CreateForm(TFormMercado, FormMercado);
  Application.Run;
end.
