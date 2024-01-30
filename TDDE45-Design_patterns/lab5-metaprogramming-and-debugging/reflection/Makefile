run: Program.exe ThirdPartyPlugin.dll
	mono Program.exe

# csc, csc-mono, etc = c-sharp-compiler

Program.exe: Program.cs PizzaInterfaces.cs
	/etc/alternatives/c-sharp-compiler Program.cs PizzaInterfaces.cs

ThirdPartyPlugin.dll: ThirdPartyPlugin.cs Program.exe
	/etc/alternatives/c-sharp-compiler -target:library ThirdPartyPlugin.cs -reference:Program.exe

clean:
	rm Program.exe ThirdPartyPlugin.dll
