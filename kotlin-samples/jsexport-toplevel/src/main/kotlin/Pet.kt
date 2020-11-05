
//@JsExport - enabling this would result in:
//            java.lang.IllegalStateException: Can't find name for declaration CLASS CLASS name:Cat \
//                modality:FINAL visibility:public superTypes:[<root>.Pet]
sealed class Pet {

    fun doCuteStuff() {}

//    @JsExport - this fix attempt is not allowed
    class Cat : Pet() {
        fun ignoreHuman() {}
    }

//    @JsExport
    class Dog : Pet() {
        fun tailHuman() {}
    }

}

// @JsExport - same error as Pet
abstract class BigCat {

    fun chill() {}

    class Lion : BigCat() {
        fun beKingly() {}
    }

    class Tiger : BigCat() {
        fun beSneaky() {}
    }

}

@JsExport // interestingly, this works fine, and includes the CareTaker
interface Humanoid {

    val name: String

    class CareTaker(val h: Humanoid) {
        fun takeCare() {}
    }

}
