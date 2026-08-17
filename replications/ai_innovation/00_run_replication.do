version 18.0
set more off

capture log close _all

foreach pkg in logout esttab reghdfe ivreghdfe {
    capture which `pkg'
    if _rc {
        di as txt "Installing missing package: `pkg'"
        if "`pkg'" == "esttab" {
            ssc install estout, replace
        }
        else {
            ssc install `pkg', replace
        }
    }
}

do 程序.do