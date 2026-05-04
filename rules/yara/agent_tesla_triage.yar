rule MAL_Triage_AgentTesla_Like_DotNet_Infostealer
{
    meta:
        description = "Triage-level detection for suspicious .NET infostealer-like samples"
        author = "Owls Hippie"
        date = "2026-05-04"
        usage = "Educational and defensive security use only"
        confidence = "low_to_medium"
        note = "This rule is a sanitized sample and requires validation before operational use."

    strings:
        $mz = { 4D 5A }
        $dotnet_1 = "mscoree.dll" ascii nocase
        $dotnet_2 = ".NETFramework" ascii nocase

        $stealer_1 = "GetPasswords" ascii nocase
        $stealer_2 = "Chrome" ascii nocase
        $stealer_3 = "Firefox" ascii nocase
        $stealer_4 = "Credentials" ascii nocase
        $stealer_5 = "SmtpClient" ascii nocase
        $stealer_6 = "NetworkCredential" ascii nocase

    condition:
        $mz at 0 and
        1 of ($dotnet_*) and
        3 of ($stealer_*)
}