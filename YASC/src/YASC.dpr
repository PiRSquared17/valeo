program YASC;

uses
  Forms,
  main in '..\..\YASC\src\main.pas' {MainForm};

{$R *.res}

begin
  Application.Initialize;
  Application.CreateForm(TMainForm, MainForm);
  Application.Run;
end.
