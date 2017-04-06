public class DayFour {
    private int age;	
  
	public void Person(int initialAge) {
  		if (initialAge > 0) {
            age = initialAge;
        } else {
            age = 0;
            System.out.println("Age is not valid, setting age to 0.");
        }
	}

	public void amIOld() {
  		// Write code determining if this person's age is old and print the correct statement:
        if (age < 13) {
            System.out.println("You are young.");
        } else if (age > 12 && age < 18) {
            System.out.println("You are a teenager.");
        } else {
            System.out.println("You are old.");
        }
	}

	public void yearPasses() {
        age++;
	}
}
