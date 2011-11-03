object FValidaEAN: TFValidaEAN
  Left = 452
  Top = 288
  BorderIcons = [biSystemMenu, biMinimize]
  Caption = 'Validar C'#243'digo de Barras (EAN13)'
  ClientHeight = 91
  ClientWidth = 270
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'MS Sans Serif'
  Font.Style = []
  OldCreateOrder = False
  OnShow = FormShow
  PixelsPerInch = 96
  TextHeight = 13
  object Label1: TLabel
    Left = 19
    Top = 69
    Width = 32
    Height = 13
    Alignment = taCenter
    Caption = 'Label1'
    Color = clBtnFace
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clRed
    Font.Height = -11
    Font.Name = 'MS Sans Serif'
    Font.Style = []
    ParentColor = False
    ParentFont = False
  end
  object Label2: TLabel
    Left = 118
    Top = 48
    Width = 32
    Height = 13
    Caption = 'Label2'
  end
  object Label3: TLabel
    Left = 19
    Top = 48
    Width = 92
    Height = 13
    Caption = 'N'#250'meros Digitados:'
  end
  object ButtonSair: TButton
    Left = 184
    Top = 32
    Width = 75
    Height = 25
    Caption = '&Sair'
    TabOrder = 1
    OnClick = ButtonSairClick
  end
  object EditCodigoBarra: TEdit
    Left = 18
    Top = 16
    Width = 125
    Height = 21
    CharCase = ecUpperCase
    MaxLength = 13
    TabOrder = 0
    OnChange = EditCodigoBarraChange
    OnKeyPress = EditCodigoBarraKeyPress
  end
end
