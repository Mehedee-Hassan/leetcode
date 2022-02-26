package slidingwindow;

import java.util.Arrays;
import java.util.Collection;
import java.util.List;
import java.util.stream.Collectors;

public class StringManipulation {
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
	
		
		String animals = "Dog,Cat,Bird";
		List<String> animalCollection = Arrays.asList(animals.split(","));
		Collection<String> animalCollection2 = Arrays.asList(animals.split(","));
		
		System.out.println(animalCollection);
		
		String stringAnimalAgain = animalCollection.stream().collect(Collectors.joining(",")); // adding to string using stream()
		
		
		System.out.println(stringAnimalAgain);
		
	}
	
}
