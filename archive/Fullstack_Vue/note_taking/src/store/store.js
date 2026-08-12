import Vue from "vue";
import Vuex from "vuex";


Vue.use(Vuex);

export const store = new Vuex.Store({
    
    state: {
        notes: [],
        timestamps: [],
    },
    getters: {
        getNotes(state) {
            return state.notes;
        },
        getTimestamps(state) {
            return state.timestamps;
        },
        getNoteCount(state) {
            return state.notes.length;
        },
    },
    mutations: {
        addNote(state, payload) {
            let newNote = payload;
            state.notes.push(newNote);
        },
        addTimestamp(state, payload) {
            let newTimeStamp = payload;
            state.timestamps.push(newTimeStamp);
        },
    },
    actions: {
        addNote(context, payload) {
            context.commit('addNote', payload)
        },
        addTimestamp(context, payload) {
            context.commit('addTimestamp', payload)
        }
    },
    modules: {

    }
})