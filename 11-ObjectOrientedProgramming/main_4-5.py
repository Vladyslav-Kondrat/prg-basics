from termometer import Termometer

def main():
    termometer = Termometer("Philips")
    termometer.degree_meter()
    termometer.termometer_on()
    termometer.degree_meter()
    termometer.termometer_off()



if __name__ == "__main__":
    main()
