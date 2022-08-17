<template>
  <v-card-text>
    <v-row justify="center" align="center" dense>
      <v-col cols="12" sm="8" md="4" lg="4">
        <div align="center" class="font-weight-bold text-capitalize">
          <h2>Log In to Cities Wishlist</h2>
          <br />
        </div>
        <v-form ref="login">
          <v-text-field
            label="Username"
            name="username"
            type="email"
            class="rounded-0"
            v-model="form.username"
          >
          </v-text-field>
          <v-text-field
            label="Password"
            name="password"
            type="password"
            class="rounded-0"
            v-model="form.password"
          ></v-text-field>
          <v-btn class="rounded-0" x-large block color="green" type="submit"
            >Login</v-btn
          >
          <br />
          <p v-if="showError" id="error-message">{{ error_message }}</p>
        </v-form>
      </v-col>
    </v-row>
  </v-card-text>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "Login",
  data: () => ({
    form: {
      username: "",
      password: "",
    },
    showError: false,
  }),
  methods: {
    checkLogin() {
      if (this.input.username == "admin" && this.input.password == "admin") {
        this.$router.push("/app");
      } else {
        this.error_message = "Wrong username or password";
      }
    },
    ...mapActions(["Login"]),
    async submit() {
      const User = new FormData();
      User.append("username", this.form.username);
      User.append("password", this.form.password);
      try {
        await this.Login(User);
        this.$router.push("/app");
        this.showError = false;
      } catch (error) {
        this.showError = true;
      }
    },
  },
};
</script>
<style scoped>
#error-message {
  color: red;
}
</style>
