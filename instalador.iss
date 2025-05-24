[Setup]
AppName=MiAplicacionCRM
AppVersion=1.0
DefaultDirName={pf}\MiAplicacionCRM
DefaultGroupName=MiAplicacionCRM
OutputDir=.
OutputBaseFilename=Instalador_MiApp
Compression=lzma
SolidCompression=yes

[Files]
Source: "app.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "db.sqlite3"; DestDir: "{app}"; Flags: ignoreversion
Source: "iniciar_app.bat"; DestDir: "{app}"; Flags: ignoreversion
Source: "static\*"; DestDir: "{app}\static"; Flags: recursesubdirs ignoreversion
Source: "templates\*"; DestDir: "{app}\templates"; Flags: recursesubdirs ignoreversion
Source: "python-3.13.3-embed-amd64\*"; DestDir: "{app}\python-3.13.3-embed-amd64"; Flags: recursesubdirs ignoreversion

[Icons]
Name: "{group}\Mi Aplicación CRM"; Filename: "{app}\iniciar_app.bat"
Name: "{group}\Desinstalar Mi Aplicación CRM"; Filename: "{uninstallexe}"
