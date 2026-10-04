@echo off
rem Test WaterFrost functionality.
rem This script verifies that watermark can be successfully embedded into a picture
rem and subsequently extracted using a password.

rem Move to the folder of the current batch scrip
cd %~dp0

rem Clear the output directory.
rem Check if output directory exists and remove it with all its content.
if exist ".\output" (
    rd /s /q ".\output"
)

rem Run WaterFrost CLI (embed example)
.\..\.venv\Scripts\python.exe .\..\main_cli.py embed --input carrier.jpg --watermark asset.txt --password NotSecretPassword --output output\watermarked.png
if %ERRORLEVEL% neq 0 (
    exit /b %ERRORLEVEL%
)

rem Run WaterFrost CLI (extract example)
.\..\.venv\Scripts\python.exe .\..\main_cli.py extract --input output\watermarked.png --password NotSecretPassword --output output\asset_recovered.txt
if %ERRORLEVEL% neq 0 (
    exit /b %ERRORLEVEL%
)

rem Compare the files to check if the watermark was successfully extracted.
fc "asset.txt" "output\asset_recovered.txt" > output\report.txt
if %ERRORLEVEL% neq 0 (
    echo FAILED: The recovered asset does not match the original.
    exit -1
)

echo SUCCESS: The recovered asset is identical to the original.
exit 0
