plugins {
    id("org.jetbrains.kotlin.js") version "1.4.10"
    kotlin("plugin.serialization") version "1.4.10"
}

repositories {
    mavenCentral()
}

dependencies {
    implementation(kotlin("stdlib-js"))
    implementation("org.jetbrains.kotlinx:kotlinx-serialization-json-js:1.0.1")
}

kotlin {
    js(IR) {
        nodejs()
        binaries.executable()
    }
}