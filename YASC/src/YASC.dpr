program YASC;

uses
  Forms,
  main in '..\..\YASC\src\main.pas' {MainForm};

{$R *.res}

begin
  Application.Initialize;
  Application.Title := 'YASC';
  Application.CreateForm(TMainForm, MainForm);
  Application.Run;
end.
