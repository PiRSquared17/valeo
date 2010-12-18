unit xkcd_unit;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, OleCtrls, SHDocVw, Buttons, Menus, ExtDlgs;

type
  Txkcd_form = class(TForm)
    BitBtnClose: TBitBtn;
    WebBrowser1: TWebBrowser;
    EditURL: TEdit;
    procedure BitBtnCloseClick(Sender: TObject);
    procedure FormCreate(Sender: TObject);
    procedure WebBrowser1NavigateComplete2(ASender: TObject;
      const pDisp: IDispatch; var URL: OleVariant);
    procedure EditURLKeyDown(Sender: TObject; var Key: Word;
      Shift: TShiftState);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  xkcd_form: Txkcd_form;

implementation

{$R *.dfm}

procedure Txkcd_form.BitBtnCloseClick(Sender: TObject);
begin
   Close;
end;

procedure Txkcd_form.EditURLKeyDown(Sender: TObject; var Key: Word;
  Shift: TShiftState);
begin
   if Key = VK_RETURN then
      WebBrowser1.Navigate(EditURL.Text);
end;

procedure Txkcd_form.FormCreate(Sender: TObject);
begin
   WebBrowser1.Align := alClient;
   WebBrowser1.Navigate('http://www.xkcd.com');
end;

procedure Txkcd_form.WebBrowser1NavigateComplete2(ASender: TObject;
  const pDisp: IDispatch; var URL: OleVariant);
begin
   EditURL.Text := WebBrowser1.LocationURL;
end;

end.
