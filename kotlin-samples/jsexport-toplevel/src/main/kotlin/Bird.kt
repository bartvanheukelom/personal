// this gives the desired result, all 6 types exported, properly namespaced
@file:JsExport

sealed class Bird {

    fun layEgg() {}

    class Duck : Bird() {
        fun swim() {}
    }

    class Chicken : Bird() {
        fun roost() {}
    }

}

abstract class AbstractBird {

    fun layAbstractEgg() {}

    class SchrodingersDuck : AbstractBird() {
        fun swimOrDont() {}
    }

    class WildGooseChaseGoose : AbstractBird() {
        fun stressOut() {}
    }

}

interface AnimalLike {

    val name: String

    class CareTaker(val a: AnimalLike) {
        fun takeCare() {}
    }

}

data class Android(val memory: String) {

    class Cloner(val template: Android) {
        fun produceClone() = template.copy()
    }

}
