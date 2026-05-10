rule MAL_Triage_LummaStealer_Like_Infostealer
{
    meta:
        description = "Triage-level detection for Lumma-like infostealer characteristics"
        author = "Damin"
        date = "2026-05-10"
        usage = "Educational and defensive security use only"
        confidence = "low_to_medium"
        note = "This rule is a sanitized sample and requires validation before operational use."

    strings:
        $mz = { 4D 5A }

        $browser_1 = "Chrome" ascii nocase
        $browser_2 = "Firefox" ascii nocase
        $browser_3 = "Login Data" ascii nocase
        $browser_4 = "Local State" ascii nocase

        $wallet_1 = "wallet" ascii nocase
        $wallet_2 = "crypto" ascii nocase

        $net_1 = "http" ascii nocase
        $net_2 = "POST" ascii nocase

    condition:
        $mz at 0 and
        2 of ($browser_*) and
        1 of ($wallet_*) and
        1 of ($net_*)
}