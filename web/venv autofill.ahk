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

^F9::
	if Winexist("Command Prompt") 
	{
		winact("Command Prompt")
	}
	else if Winexist("Windows PowerShell") 
	{
		winact("Windows PowerShell")
	}
return


winact(window)
{ 
	Sleep, 55 
	WinActivate, %window%
	Sleep, 133  
	Send, {c Down}{d Down}{c Up}{d Up}{Space Down}{Space Up}{v Down}{e Down}{n Down}{v Up}{e Up}{n Up}{Tab Down}{Tab Up}{Enter Down}{Enter Up}{c Down}{d Down}{c Up}{d Up}{Space Down}{Space Up}{s Down}{c Down}{s Up}{c Up}{r Down}{r Up}{i Down}{p Down}{i Up}{p Up}{Tab Down}{Tab Up}{Enter Down}{Enter Up}{a Down}{c Down}{a Up}{c Up}{Tab Down}{Tab Up}{Enter Down}{Enter Up}{c Down}{d Down}{c Up}{d Up}{Space Down}{Space Up}{. Down}{. Up}{. Down}{. Up}{/ Down}{. Down}{. Up}{. Down}{. Up}{Enter Down}{Enter Up}
	Return
}