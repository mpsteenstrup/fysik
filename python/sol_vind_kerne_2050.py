import matplotlib.pyplot as plt

# nuclear
# https://www.iaea.org/newscenter/pressreleases/iaea-outlook-for-nuclear-power-increases-for-fourth-straight-year-adding-to-global-momentum-for-nuclear-expansion

# solar
# https://www.iea.org/news/iea-sees-great-potential-for-solar-providing-up-to-a-quarter-of-world-electricity-by-2050

# wind 10 gange i dag
# https://www.unep.org/news-and-stories/story/new-report-envisages-10-fold-increase-global-wind-power-2050

# Energy consumption
# https://ourworldindata.org/energy-production-consumption

E_nuclear_GWh_2023 = 6824*1000 
E_solar_GWh_2023 = 4264*1000
E_wind_GWh_2023 = 6040*1000
E_hydro_GWh_2023 = 11014*1000


# 2050 mest optimistiske estimater
E_nuclear_GWh = E_nuclear_GWh_2023*2.5 
E_solar_GWh = 9000*1000
E_wind_GWh = E_wind_GWh_2023*10
E_hydro_GWh = E_hydro_GWh_2023*1.04**25

# energiforbrug sat til det samme som 2023
E_use = 183230*1000 # GWh
# E_use_2050 = E_use*1.05**25

print((E_nuclear_GWh+E_wind_GWh+E_solar_GWh+E_hydro_GWh)/E_use*100)

# Labels and sizes for the pie charts
labels = ['Nuclear', 'Solar', 'Wind', 'Hydro', 'Other']
sizes_2050 = [E_nuclear_GWh, E_solar_GWh, E_wind_GWh, E_hydro_GWh, E_use - (E_nuclear_GWh + E_solar_GWh + E_wind_GWh + E_hydro_GWh)]

sizes_2023 = [E_nuclear_GWh_2023, E_solar_GWh_2023, E_wind_GWh_2023, E_hydro_GWh_2023, E_use - (E_nuclear_GWh_2023 + E_solar_GWh_2023 + E_wind_GWh_2023 + E_hydro_GWh_2023)]

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(20, 7))

# 2050 pie chart as part of total energy use
axs[1].pie(sizes_2050, labels=labels, autopct='%1.1f%%', startangle=140)
axs[1].set_title('Energy Distribution by 2050')

# 2023 pie chart
axs[0].pie(sizes_2023, labels=labels, autopct='%1.1f%%', startangle=140)
axs[0].set_title('Energy Distribution in 2023')

# Equal aspect ratio ensures that pie is drawn as a circle.
for ax in axs:
    ax.axis('equal')

# Display the charts
plt.show()
