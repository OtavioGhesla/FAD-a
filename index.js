import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'Home',
            component: ()=> Home
        },
        {
            path: '/login',
            name: 'Login',
            component: ()=> import ('../views/Login.vue')
        },
        {
            path: '/signup',
            name: 'Signup',
            component: ()=> import ('../views/Signup.vue')
        },
        {
            path: '/history',
            name: 'History',
            component: ()=> import ('../views/History.vue'),
            beforeEnter: (to, from, next) => {
                const token = localStorage.getItem('token');
                if (token) {
                  next();
                } else {
                  next({ name: 'Login' });
                }
              }
        },
        {
            path: '/tutorial',
            name: 'Tutorial',
            component: ()=> import ('../views/Tutorial.vue')
        },
        {
            path: '/overview',
            name: 'Overview',
            component: ()=> import ('../views/Overview.vue')
        },
        {
            path: '/overview/dockerfile',
            name: 'Dockerfile',
            component: ()=> import ('../views/Frameworks.vue')
        },
        {
            path: '/overview/dockercompose',
            name: 'DockerCompose',
            component: ()=> import ('../views/Dockercompose.vue')
        }
    ]
})

export default router
