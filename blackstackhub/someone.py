class Smth():
    def add_run(self, paragraph):
        return paragraph

names_variable = ',"Alice", "Bob", "Charlie",'

p = Smth()

run = p.add_run('''
{what}
public class UserInformation {{
    public static void main(String[] args) {{
        // Define user information
        String[] names = {{{names_variable}}};
        int[] ages = {{25, 30, 22}};
        String[] dobs = {{"1997-05-15", "1992-11-28", "2000-03-10"}};

        // Loop through the users and print information
        for (int i = 0; i < names.length; i++) {{
            System.out.println("Username: " + names[i]);
            System.out.println("Age: " + ages[i]);
            System.out.println("DOB: " + dobs[i]);
            System.out.println(); // Add an empty line for separation
        }}
    }}
}}
'''.format(what="water?", names_variable='["Alice", "Bob", "Charlie"]'))
print(run)
