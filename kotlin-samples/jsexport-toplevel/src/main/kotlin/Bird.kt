// this gives the desired result, all 3 types exported, properly namespaced
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
