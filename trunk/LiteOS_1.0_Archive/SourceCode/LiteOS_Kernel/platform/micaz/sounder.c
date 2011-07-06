/* The LiteOS Operating System Kernel */
/*
   The following is the license of LiteOS.
   This file is part of LiteOS.
   LiteOS is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   LiteOS is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   You should have received a copy of the GNU General Public License
   along with LiteOS.  If not, see <http://www.gnu.org/licenses/>.
 */
 
/* Author Qi Mi (qm8e@virginia.edu) */

#include "../avr/avrhardware.h"
#include "micazhardware.h"
#include "sounder.h"
#include "../../utilities/eventlogger.h"
//--------------------------------------
void micaz_sounder()
{
    //activate the sounder
    {
        _atomic_t _atomic = _atomic_start();

        LITE_MAKE_PW2_OUTPUT();
        _atomic_end(_atomic);
    }
}

//--------------------------------------
void micaz_sounderOn()
{
    {
        _atomic_t _atomic = _atomic_start();

        micaz_sounder();
        LITE_SET_PW2_PIN();
        _atomic_end(_atomic);
    }
    return;
}

//--------------------------------------
void micaz_sounderOff()
{
    {
        _atomic_t _atomic = _atomic_start();

        micaz_sounder();
        LITE_CLR_PW2_PIN();
        _atomic_end(_atomic);
    }
    return;
}