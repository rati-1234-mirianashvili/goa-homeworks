// toUpperCase() - ტექსტის ყველა ასოს დიდ ასოდ გარდაქმნის
console.log("hello".toUpperCase()); // HELLO
console.log("javascript".toUpperCase()); // JAVASCRIPT

// toLowerCase() - ტექსტის ყველა ასოს პატარა ასოდ გარდაქმნის
console.log("HELLO".toLowerCase()); // hello
console.log("JAVASCRIPT".toLowerCase()); // javascript

// startsWith() - ამოწმებს, იწყება თუ არა ტექსტი მითითებული სიმბოლოებით
console.log("JavaScript".startsWith("Java")); // true
console.log("Html".startsWith("Back")); // false

// endsWith() - ამოწმებს, მთავრდება თუ არა ტექსტი მითითებული სიმბოლოებით
console.log("JavaScript".endsWith("Script")); // true
console.log("Html".endsWith("Back")); // false

// trim() - შლის ზედმეტ გამოტოვებებს ტექსტის დასაწყისიდან და ბოლოდან
console.log("  Hello  ".trim()); // "Hello"
console.log("  World  ".trim()); // "World"

// trimEnd() - შლის გამოტოვებებს მხოლოდ ტექსტის ბოლოდან
console.log("Hello   ".trimEnd()); // "Hello"
console.log("JavaScript   ".trimEnd()); // "JavaScript"

// trimStart() - შლის გამოტოვებებს მხოლოდ ტექსტის დასაწყისიდან
console.log("   Hello".trimStart()); // "Hello"
console.log("   World".trimStart()); // "World"