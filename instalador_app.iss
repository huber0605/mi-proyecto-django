[Setup]
AppName=Django CRM
AppVersion=1.0
DefaultDirName={autopf}\DjangoCRM
DefaultGroupName=Django CRM
OutputDir=.
OutputBaseFilename=instalador_crm
Compression=lzma
SolidCompression=yes

[Files]
Source: "instalador_app\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Django CRM"; Filename: "{app}\app.exe"
Name: "{group}\Desinstalar Django CRM"; Filename: "{uninstallexe}"
