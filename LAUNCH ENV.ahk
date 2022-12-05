#NoEnv
SetWorkingDir %A_ScriptDir%
CoordMode, Mouse, Window
SendMode Input
#SingleInstance Force
SetTitleMatchMode 2
#WinActivateForce
SetControlDelay 1
SetWinDelay 0
SetKeyDelay -1
SetMouseDelay -1
SetBatchLines -1
 
if Winexist("Command Prompt") 
{
	winact("Command Prompt")
}
else if Winexist("Windows PowerShell") 
{
	winact("Windows PowerShell")
} 
else
{
	Run, powershell.exe -NoExit -Command ""
	loop, 20
	{
		if Winexist("Windows PowerShell")
		{
			winact("Windows PowerShell")
			break
		}
		sleep 100
	}
}


winact(window)
{ 
	appname := "main.py"
	Sleep, 55 
	WinActivate, %window%
	Sleep, 22  
	Send, {c Down}{d Down}{c Up}{d Up}{Space Down}{Space Up}{v Down}{e Down}{n Down}{v Up}{e Up}{n Up}{Tab Down}{Tab Up}{Enter Down}{Enter Up}{c Down}{d Down}{c Up}{d Up}{Space Down}{Space Up}{s Down}{c Down}{s Up}{c Up}{r Down}{r Up}{i Down}{p Down}{i Up}{p Up}{Tab Down}{Tab Up}{Enter Down}{Enter Up}{a Down}{c Down}{a Up}{c Up}{Tab Down}{Tab Up}{Enter Down}{Enter Up}{c Down}{d Down}{c Up}{d Up}{Space Down}{Space Up}{. Down}{. Up}{. Down}{. Up}{/ Down}{. Down}{. Up}{. Down}{. Up}{Enter Down}{Enter Up}
	
	sleep, 50
	WinActivate, %window%
	Send, {c Down}{d Down}{c Up}{d Up}{space Down}{space up}{e down}{x down}{a down}{e up}{x up}{a up}{tab down}{tab up}{enter down}{enter up}
	Send, {p Down}{y Down}{p Up}{y Up}{space Down}{space up}
	sendraw, %appname%
	send, {enter Down}{enter Up}
	Return
}