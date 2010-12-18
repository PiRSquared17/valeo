program xkcd;

uses
  Forms,
  xkcd_unit in 'xkcd_unit.pas' {xkcd_form};

{$R *.res}

begin
  Application.Initialize;
  Application.MainFormOnTaskbar := True;
  Application.CreateForm(Txkcd_form, xkcd_form);
  Application.Run;
end.
