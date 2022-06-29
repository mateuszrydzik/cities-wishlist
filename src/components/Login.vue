<template>
  <v-card-text>
    <v-row justify="center" align="center" dense>
      <v-col cols="12" sm="8" md="4" lg="4">
        <div align="center" class="font-weight-bold text-capitalize">
          Login to access app
        </div>
        <v-form ref="login">
          <v-text-field
            label="Username"
            name="username"
            type="email"
            class="rounded-0"
            v-model="input.username"
          >
          </v-text-field>
          <v-text-field
            label="Password"
            name="password"
            type="password"
            class="rounded-0"
            v-model="input.password"
          ></v-text-field>
          <v-btn
            class="rounded-0"
            x-large
            block
            color="green"
            @click="consoleLog()"
            >Login</v-btn
          >
        </v-form>
      </v-col>
    </v-row>
  </v-card-text>
</template>

<script>
export default {
  name: "Login",
  data: () => ({
    input: {
      username: "",
      password: "",
    },
  }),
  methods: {
    checkLogin() {
      if (
        this.input.username == this.$parent.admAccount.username &&
        this.input.password == this.$parent.admAccount.password
      ) {
        console.log("success!");
      } else {
        console.log("fail");
      }
    },
    consoleLog() {
      console.log(this.$parent.username);
    },
  },
};
</script>
