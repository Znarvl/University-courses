Running the lab
===============

The source code are without project files for monodevelop, etc.
This is for simplicity. You can load all 3 files in monodevelop and comment
out loading the dll if you want to test things first. But to pass the lab,
you should load some classes at runtime.

```
csc Program.cs PizzaInterfaces.cs
csc -target:library ThirdPartyPlugin.cs -reference:Program.exe
mono Program.exe # Or just run the .exe-file on Windows
```

If running Linux, you can also do
```
make run
```
