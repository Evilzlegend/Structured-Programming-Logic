if itemsOrdered <= RANGE1 then
    customerDiscount = DISCOUNT1
else
    if itemsOrdered <= RANGE2 then
        customerDiscount = DISCOUNT2
    else
        if itemsOrdered <= RANGE3 then
            customerDiscount = DISCOUNT3
        else
            customerDiscount = DISCOUNT4
        endif
    endif
endif
