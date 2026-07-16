# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_water_reminder.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: fbiber <fbiber@student.42istanbul.com.tr>   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/19 19:43:46 by fbiber             #+#    #+#             #
#   Updated: 2026/04/20 13:54:44 by fbiber            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_water_reminder() -> None:
    lastwatering = int(input("Day since last watering: "))
    if lastwatering > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
