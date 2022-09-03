# Lab 1. Install and Configure an Integrated Development Environment (IDE) for Python Development

## Installation of Chocolatey package manager

As I am using MS Windows, in this short tutorial we will use Chocolatey to set up our Python Environment.

1. Use this link to go to the [Chocolatey install web page](https://chocolatey.org/install)

- We will use the Individual version
  ![Chocolatey Website](MSIT5214-01-Algorithms\img\Unit1\Lab1\ChocolateyInstallation.png)

2. In your windows desktop, Run PowerShell as Administrator

![PowerShell Administrator](MSIT5214-01-Algorithms\img\Unit1\Lab1\powershell-admin.png)

- Execute the following command:

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

3. Once succesfully completed, type

```powershell
choco -?
```

4. You will see the multiple options for running the Chocolatey Command Line Interfacer (CLI)

## Installation of Python using Chocolatey

1. To install the latest Python version, type:

```powershell
choco install python
```

- You will see an output like this. I recommend you to type the letter 'A' + enter to continue with the installation

```powershell
Chocolatey v1.1.0
Installing the following packages:
python
By installing, you accept licenses for the packages.
Progress: Downloading python3 3.10.6... 100%
Progress: Downloading python 3.10.6... 100%
python3 v3.10.6 [Approved]
python3 package files install completed. Performing other installation steps.
The package python3 wants to run 'chocolateyInstall.ps1'.
Note: If you don't run this script, the installation will fail.
Note: To confirm automatically next time, use '-y' or consider:
choco feature enable -n allowGlobalConfirmation
Do you want to run the script?([Y]es/[A]ll - yes to all/[N]o/[P]rint):
```

- After the installation finishes, you will see the following lines:

```powershell
 The install of python was successful.
  Software installed to 'C:\ProgramData\chocolatey\lib\python'

Chocolatey installed 1/1 packages.
 See the log for details (C:\ProgramData\chocolatey\logs\chocolatey.log).
```

2.  To confirm python was correctly installed, type:

```powershell
python --version
```

- The output will be:

```powershell
Python 3.10.6
```

## Installation of IntelliJ IDEA Community Edition

1. To install IntelliJ IDE Community Edition, let's type the following command:

```powershell
choco install intellijidea-community
```

- The output will be:

```powershell
Chocolatey v1.1.0
Installing the following packages:
intellijidea-community
By installing, you accept licenses for the packages.
Progress: Downloading intellijidea-community 2022.2.1... 100%

intellijidea-community v2022.2.1 [Approved]
intellijidea-community package files install completed. Performing other installation steps.
The package intellijidea-community wants to run 'chocolateyInstall.ps1'.
Note: If you don't run this script, the installation will fail.
Note: To confirm automatically next time, use '-y' or consider:
choco feature enable -n allowGlobalConfirmation
Do you want to run the script?([Y]es/[A]ll - yes to all/[N]o/[P]rint):
```

Type A and the enter key to perform the installation. It will take some minutes depending your internet speed.

After the installation finished succesfully, you will see this message:

```powershell
The install of intellijidea-community was successful.
Software installed to 'C:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2022.2.1'
Chocolatey installed 1/1 packages.
See the log for details (C:\ProgramData\chocolatey\logs\chocolatey.log).
```

## Installation of Visual Studio Code

. To install the Visual Studio Code IDE, type the following command:

```powershell
choco install vscode
```

- The output will be:

```powershell
Chocolatey v1.1.0
Installing the following packages:
vscode
By installing, you accept licenses for the packages.
Progress: Downloading vscode.install 1.70.2... 100%
Progress: Downloading DotNet4.5.2 4.5.2.20140902... 100%
Progress: Downloading vscode 1.70.2... 100%

DotNet4.5.2 v4.5.2.20140902 [Approved]
dotnet4.5.2 package files install completed. Performing other installation steps.
The package DotNet4.5.2 wants to run 'ChocolateyInstall.ps1'.
Note: If you don't run this script, the installation will fail.
Note: To confirm automatically next time, use '-y' or consider:
choco feature enable -n allowGlobalConfirmation
Do you want to run the script?([Y]es/[A]ll - yes to all/[N]o/[P]rint):
```

Type A and the enter key to perform the installation. It will take some minutes depending your internet speed.

After the installation finished succesfully, you will see this message:

```powershell
Microsoft .Net 4.5.2 Framework is already installed on your machine.
 The install of dotnet4.5.2 was successful.
  Software install location not explicitly set, it could be in package or
  default install location of installer.

vscode.install v1.70.2 [Approved]
vscode.install package files install completed. Performing other installation steps.
Merge Tasks: !runCode, desktopicon, quicklaunchicon, addcontextmenufiles, addcontextmenufolders, associatewithfiles, addtopath
Downloading vscode.install 64 bit
  from 'https://az764295.vo.msecnd.net/stable/e4503b30fc78200f846c62cf8091b76ff5547662/VSCodeSetup-x64-1.70.2.exe'
Progress: 100% - Completed download of D:\Users\vicrojo\AppData\Local\Temp\chocolatey\vscode.install\1.70.2\VSCodeSetup-x64-1.70.2.exe (79.04 MB).
Download of VSCodeSetup-x64-1.70.2.exe (79.04 MB) completed.
Hashes match.
Installing vscode.install...
vscode.install has been installed.
  vscode.install can be automatically uninstalled.
 The install of vscode.install was successful.
  Software installed to 'C:\Program Files\Microsoft VS Code\'

vscode v1.70.2 [Approved]
vscode package files install completed. Performing other installation steps.
 The install of vscode was successful.
  Software installed to 'C:\ProgramData\chocolatey\lib\vscode'

Chocolatey installed 3/3 packages.
 See the log for details (C:\ProgramData\chocolatey\logs\chocolatey.log).
```
