object MainForm: TMainForm
  Left = 207
  Top = 192
  BorderStyle = bsDialog
  Caption = 'Yet Another Supermarket Control'
  ClientHeight = 423
  ClientWidth = 729
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
  object BitBtnSair: TBitBtn
    Left = 240
    Top = 352
    Width = 177
    Height = 40
    Caption = 'Sair'
    DoubleBuffered = True
    ParentDoubleBuffered = False
    TabOrder = 0
    OnClick = BitBtnSairClick
  end
  object ZConnection: TZConnection
    Protocol = 'postgresql-8'
    HostName = 'localhost'
    Database = 'copa2014'
    User = 'postgres'
    Password = 'zapzap'
    AutoCommit = False
    ReadOnly = True
    Connected = True
    Left = 134
    Top = 224
  end
  object ZSupermercado: TZQuery
    Connection = ZConnection
    SQL.Strings = (
      'select * from cargo')
    Params = <>
    Left = 514
    Top = 225
    object ZSupermercadocodigo: TIntegerField
      FieldName = 'codigo'
      Required = True
    end
    object ZSupermercadodescricao: TWideStringField
      FieldName = 'descricao'
      Size = 80
    end
  end
  object ZSQLMetadata: TZSQLMetadata
    Connection = ZConnection
    MetadataType = mdProcedures
    Left = 202
    Top = 224
  end
  object DSSQLMetadata: TDataSource
    DataSet = ZSupermercado
    Left = 414
    Top = 224
  end
  object ZSQLMonitor: TZSQLMonitor
    Active = True
    MaxTraceCount = 100
    Left = 274
    Top = 226
  end
end
