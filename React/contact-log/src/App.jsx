import catimage1 from "/Users/akshad/GitHub/Workspace/React/contact-log/src/assets/cat.jpeg";
import catimage2 from "/Users/akshad/GitHub/Workspace/React/contact-log/src/assets/cat2.jpg";
import catimage3 from "/Users/akshad/GitHub/Workspace/React/contact-log/src/assets/cat3.jpeg";
import catimage4 from "/Users/akshad/GitHub/Workspace/React/contact-log/src/assets/cat4.jpg";
import phoneimage1 from "/Users/akshad/GitHub/Workspace/React/contact-log/src/assets/phone.png";
import mailimage1 from "/Users/akshad/GitHub/Workspace/React/contact-log/src/assets/mail.png";
import Contact from "./contact";
export default function App() {
  return (
    <div className="contacts">
      <Contact
        img={catimage1}
        name="Mr. Whiskerson"
        phone="(212) 555-1234"
        email="mr.whiskaz@catnap.meow"
      />
      <Contact
        img={catimage2}
        name="Fluffykins"
        phone="(212) 555-2345"
        email="fluff@me.com"
      />
      <Contact
        img={catimage3}
        name="Felix"
        phone="(212) 555-4567"
        email="thecat@hotmail.com"
      />
      <Contact
        img={catimage4}
        name="Pumpkin"
        phone="(0800) CAT KING"
        email="pumpkin@scrimba.com"
      />
    </div>
  );
}
