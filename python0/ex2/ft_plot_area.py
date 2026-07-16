# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_plot_area.py                                     :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: fbiber <fbiber@student.42istanbul.com.tr>   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/19 17:28:38 by fbiber             #+#    #+#             #
#   Updated: 2026/04/19 17:47:03 by fbiber            ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_plot_area() -> None:
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    sonuc = length * width
    print(f"Plot area: {sonuc}")
