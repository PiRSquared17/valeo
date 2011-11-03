program ValidaCodigoBarras;

uses
  Forms,
  ValidaEAN in 'ValidaEAN.pas' {FValidaEAN};

{$R *.RES}

begin
  Application.Initialize;
  Application.CreateForm(TFValidaEAN, FValidaEAN);
  Application.Run;
end.
