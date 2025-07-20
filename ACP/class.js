// Parent class
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    static displayInfo(person) {
        console.log(Name: ${ person.name }, Age: ${ person.age });
    }
}

// Child class inheriting from Person
class Employee extends Person {
    constructor(name, age, employeeId) {
        super(name, age);
        this.employeeId = employeeId;
    }

    displayEmployeeInfo() {
        console.log(Employee ID: ${ this.employeeId });
        Person.displayInfo(this); // Using static method from Person class
    }
}

// Create an instance of Employee
let employee = new Employee("John Doe", 30, "E123");

// Display employee information
employee.displayEmployeeInfo();
